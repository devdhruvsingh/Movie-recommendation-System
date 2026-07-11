import streamlit as st
import pickle
import pandas as pd
import requests

# 1. Page Configuration
st.set_page_config(page_title="CineMatch AI", page_icon="✨", layout="wide")

# Initialize session state for view routing
if "view_page" not in st.session_state:
    st.session_state.view_page = "dashboard"
if "selected_detail_movie" not in st.session_state:
    st.session_state.selected_detail_movie = None

# --- STATE CALLBACK FUNCTIONS (This prevents crashes) ---
def go_to_dashboard():
    st.session_state.view_page = "dashboard"

def go_to_details(movie_name):
    st.session_state.selected_detail_movie = movie_name
    st.session_state.view_page = "details"
# --------------------------------------------------------

# Securely pull the OMDb API key
API_KEY = st.secrets["OMDB_API_KEY"]

# 2. Custom CSS: Soothing Slate & Sky Blue Theme
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #e2e8f0; }
    .movie-card {
        background-color: #1e293b;
        padding: 16px;
        border-radius: 16px;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
        margin-bottom: 12px;
        text-align: center;
        border: 1px solid #334155;
        transition: transform 0.2s ease-in-out;
    }
    .movie-card:hover { transform: translateY(-5px); border-color: #38bdf8; }
    .movie-title {
        color: #f8fafc; font-size: 1.1rem; font-weight: 600;
        margin-top: 12px; margin-bottom: 6px; height: 50px; overflow: hidden;
    }
    .match-score {
        color: #38bdf8; font-weight: 700; font-size: 0.9rem; margin-bottom: 12px;
        background: rgba(56, 189, 248, 0.1); display: inline-block; padding: 4px 12px; border-radius: 20px;
    }
    .metadata-tag { color: #94a3b8; font-size: 0.95rem; margin-bottom: 5px; }
    </style>
""", unsafe_allow_html=True)

# 3. Rich Metadata Fetcher Engine
def fetch_movie_details(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("Response") == "True":
            poster = data.get("Poster")
            if poster == "N/A":
                poster = "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=500"
            return {
                "poster": poster, "plot": data.get("Plot", "No synopsis available."),
                "director": data.get("Director", "Unknown"), "actors": data.get("Actors", "Unknown"),
                "rating": data.get("imdbRating", "N/A"), "year": data.get("Year", "N/A")
            }
    except Exception:
        pass
    
    return {
        "poster": "https://images.unsplash.com/photo-1594909122845-11baa439b7bf?q=80&w=500",
        "plot": "Synopsis currently unavailable.", "director": "Unknown", "actors": "Unknown", 
        "rating": "N/A", "year": "N/A"
    }

# 4. Load Datasets
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies_df = pd.DataFrame(movies_dict)
    similarity_matrix = pickle.load(open('similarity.pkl', 'rb'))
    return movies_df, similarity_matrix

movies, similarity = load_data()

# 5. Core Recommendation Algorithm
def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    match_scores = []
    for i in movie_list:
        title = movies.iloc[i[0]].title
        recommended_movies.append(title)
        match_scores.append(int(i[1] * 100))
        
    return recommended_movies, match_scores


# =====================================================================
# VIEW 1: MOVIE DETAILS (Rich Information Page)
# =====================================================================
if st.session_state.view_page == "details":
    target_movie = st.session_state.selected_detail_movie
    
    # Utilizing the callback here instead of st.rerun()
    st.button("✨ Back to Search", on_click=go_to_dashboard)
        
    st.markdown("---")
    
    with st.spinner("Fetching studio metadata..."):
        details = fetch_movie_details(target_movie)
    
    col_img, col_info = st.columns([1, 2.5])
    
    with col_img:
        st.image(details["poster"], use_container_width=True, clamp=True)
        
    with col_info:
        st.title(f"{target_movie} ({details['year']})")
        st.markdown(f"⭐ **IMDb Rating:** {details['rating']}/10")
        st.markdown("### Synopsis")
        st.write(details["plot"])
        st.markdown("### Credits")
        st.markdown(f"<div class='metadata-tag'>🎬 <b>Director:</b> {details['director']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='metadata-tag'>🎭 <b>Cast:</b> {details['actors']}</div>", unsafe_allow_html=True)
        
    st.write("")
    st.markdown("### 🍿 More like this:")
    
    names, scores = recommend(target_movie)
    cols = st.columns(5)
    
    for idx in range(5):
        with cols[idx]:
            rec_details = fetch_movie_details(names[idx])
            st.image(rec_details["poster"], use_container_width=True)
            st.markdown(f"""
                <div class="movie-card" style="padding: 10px;">
                    <div class="movie-title" style="font-size: 0.95rem; height: 40px;">{names[idx]}</div>
                    <div class="match-score" style="font-size: 0.75rem;">🔥 {scores[idx]}% Match</div>
                </div>
            """, unsafe_allow_html=True)
            
            # Utilizing the callback here with arguments
            st.button("View", key=f"rec_det_{names[idx]}", on_click=go_to_details, args=(names[idx],), use_container_width=True)

# =====================================================================
# VIEW 2: MAIN DASHBOARD
# =====================================================================
else:
    st.title("✨ CineMatch AI")
    st.markdown("Discover your next cinematic obsession through our mathematical mapping engine.")
    st.write("")

    col_search, _ = st.columns([2, 1])
    with col_search:
        selected_movie_name = st.selectbox(
            'Search our database for a movie you love:',
            movies['title'].values,
            index=0
        )

    st.markdown("---")

    if selected_movie_name:
        with st.spinner('Scanning the matrix...'):
            names, scores = recommend(selected_movie_name)
        
        st.subheader("Your Curated Recommendations:")
        st.write("")
        
        cols = st.columns(5)
        
        for idx in range(5):
            with cols[idx]:
                rec_details = fetch_movie_details(names[idx])
                
                st.image(rec_details["poster"], use_container_width=True)
                st.markdown(f"""
                    <div class="movie-card">
                        <div class="movie-title">{names[idx]}</div>
                        <div class="match-score">🔥 {scores[idx]}% Match</div>
                    </div>
                """, unsafe_allow_html=True)
                
                # Utilizing the callback here with arguments
                st.button("Explore Details", key=f"dash_{names[idx]}", on_click=go_to_details, args=(names[idx],), use_container_width=True)