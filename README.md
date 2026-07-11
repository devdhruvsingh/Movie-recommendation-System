🎬 CineMatch AI: Intelligent Movie Recommendation Engine
CineMatch AI is a sophisticated, end-to-end recommendation system that transforms the cinematic discovery experience. By utilizing advanced natural language processing and vector space modeling, the system identifies thematic nuances between thousands of films to suggest content that genuinely aligns with user preferences.
🌟 Project Overview
CineMatch AI goes beyond simple genre matching. It treats movies as data points in a high-dimensional vector space, allowing for "Content-Based Filtering." This means if you love a complex sci-fi thriller, the engine identifies films with similar plot structures, character dynamics, and directorial signatures.
🧠 The Intelligence: Machine Learning & Data Processing
This project leverages a robust pipeline to turn raw CSV data into an intelligent recommendation engine:
Data Cleaning & Preprocessing: * Imputation: Handled missing values in plot summaries and cast metadata.
Text Normalization: Lowercased all text, removed punctuation, and stripped spaces between multi-word tags (e.g., "Christopher Nolan" becomes "ChristopherNolan") to ensure the model treats them as unique tokens.
Feature Engineering: Combined crucial metadata—Overview, Genres, Keywords, Cast, and Crew—into a single "Tag" vector for each movie.
Vectorization (Bag of Words): Converted text tags into numeric vectors using CountVectorizer, ignoring common "stop words" to focus on meaningful identifiers.
Cosine Similarity Algorithm: Used to calculate the distance between the vectors. The result is a high-performance similarity matrix where every movie has a "proximity score" relative to every other movie in the database.
🚀 Technical Stack
Core: Python 3.x
ML Library: Scikit-Learn
Frontend/UI: Streamlit (High-performance web framework)
Metadata Engine: OMDb API (Real-time data fetching)
Infrastructure: Git, Streamlit Cloud
🛠 Installation & Deployment
Follow these steps to replicate the environment on your local machine:
Clone the Repository:
Bash
git clone https://github.com/devdhruvsingh/Movie-recommendation-System.git
cd Movie-recommendation-System
Initialize Virtual Environment:
Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:
Bash
pip install -r requirements.txt
Configure API Security:
Create a hidden folder: mkdir .streamlit
Create a file: .streamlit/secrets.toml
Add your key: OMDB_API_KEY = "your_8_char_key_here"
Generate Model Data:
Open recommender.ipynb and run all cells. This script will process the CSVs and generate your movie_dict.pkl and similarity.pkl files locally.
Launch the Dashboard:
Bash
streamlit run app.py

How It Works: The Machine Learning Pipeline
The CineMatch AI engine follows a structured path from raw data ingestion to user-facing recommendations. The process is broken down into four distinct stages:
Data Ingestion & Cleaning: We start with the TMDB 5000 dataset. We normalize titles, merge credits with movie metadata, and perform text cleaning to prepare the raw information.
Feature Engineering: We perform "tag synthesis." By combining genres, keywords, and cast/crew lists into a single consolidated string, we create a rich textual representation of each movie's DNA.
Vectorization: Using CountVectorizer, we transform the textual tags into a sparse matrix of word counts. This converts semantic movie data into a format that the machine can calculate.
Similarity Engine: We apply Cosine Similarity, which measures the cosine of the angle between two vectors. The closer the vectors, the higher the similarity score, allowing the app to recommend the most relevant films.
📈 Features at a Glance
Seamless Navigation: State-managed UI allowing users to switch between the main discovery dashboard and rich, detailed movie profiles.
Real-time Metadata: Integrates live data (IMDb ratings, posters, plot, cast) so your database never feels outdated.
Responsive Performance: Implements aggressive caching (@st.cache_data) and optimized network handling to prevent application crashes during heavy API traffic.
⚖️ License
This project is open-source and available under the MIT License. Feel free to fork, enhance, and implement your own custom recommendation parameters!
