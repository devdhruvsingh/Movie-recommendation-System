# 🎬 CineMatch AI – Intelligent Movie Recommendation Engine

> **An end-to-end Machine Learning-powered movie recommendation system that helps users discover movies based on content similarity rather than popularity.**

CineMatch AI leverages **Natural Language Processing (NLP)** and **Content-Based Filtering** to recommend movies with similar themes, genres, plot structures, cast, and directorial style. Instead of relying on user ratings or collaborative filtering, the system analyzes the intrinsic characteristics of movies to generate highly relevant recommendations.

---

## 🌟 Project Overview

Finding the right movie can be overwhelming with thousands of options available. **CineMatch AI** solves this problem by treating every movie as a point in a high-dimensional vector space.

By analyzing metadata such as:

- 🎭 Genres
- 📝 Plot Overview
- 🔑 Keywords
- 🎬 Cast
- 🎥 Director & Crew

the system creates a unique representation of every movie and recommends films with the highest semantic similarity.

---

## 🚀 Demo

**Live Application:** *(Add your Streamlit link here)*

Example:

```
https://cinematch-ai.streamlit.app
```

---

# 📸 Application Preview

> Add screenshots of your application here.

### Home Page

![Home Page](images/home.png)

### Movie Details

![Movie Details](images/details.png)

---

# 🧠 Machine Learning Pipeline

The recommendation engine follows a structured machine learning workflow.

## 1️⃣ Data Collection

Dataset used:

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

The movie metadata and credits are merged into a unified dataset.

---

## 2️⃣ Data Cleaning & Preprocessing

Several preprocessing techniques were applied to improve recommendation quality.

### Missing Value Handling

- Removed null values
- Cleaned incomplete records

### Text Normalization

- Converted text to lowercase
- Removed punctuation
- Removed unnecessary spaces
- Combined multi-word entities

Example:

```
Christopher Nolan
```

becomes

```
ChristopherNolan
```

This ensures the vectorizer treats names as single meaningful tokens.

---

## 3️⃣ Feature Engineering

Instead of relying on a single feature, multiple metadata columns are combined into one rich textual representation.

The following columns are merged:

- Overview
- Genres
- Keywords
- Cast
- Crew (Director)

Example:

```
Action Adventure Hero Marvel RobertDowneyJr JonFavreau
```

This creates a unique "movie DNA" for every film.

---

## 4️⃣ Text Vectorization

The textual data is transformed into numerical vectors using **CountVectorizer** from Scikit-Learn.

### Why CountVectorizer?

It converts text into a Bag-of-Words representation while removing common English stop words.

Example:

```
Movie Tags
↓

CountVectorizer

↓

Sparse Matrix
```

Each movie becomes a vector representing the frequency of important words.

---

## 5️⃣ Similarity Calculation

The recommendation engine uses **Cosine Similarity** to calculate the similarity between movie vectors.

Movies with the highest cosine similarity scores are recommended.

```
Movie A
        \
         \  Cosine Similarity
          \
Movie B
```

The closer the vectors are, the more similar the movies.

---

# ⚙️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| Language | Python 3 |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| NLP | CountVectorizer |
| Frontend | Streamlit |
| API | OMDb API |
| Version Control | Git & GitHub |
| Deployment | Streamlit Cloud |

---

# 📂 Project Structure

```
Movie-recommendation-System/
│
├── app.py
├── recommender.ipynb
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
│
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── images/
│   ├── home.png
│   └── details.png
│
└── .streamlit/
    └── secrets.toml
```

---

# ✨ Features

### 🎬 Smart Movie Recommendations

Recommends movies based on semantic similarity rather than popularity.

---

### 📖 Detailed Movie Profiles

Displays

- Movie Poster
- IMDb Rating
- Plot
- Runtime
- Release Date
- Cast
- Director

using live data from the OMDb API.

---

### ⚡ Fast Performance

Optimized using

- `@st.cache_data`
- Cached API calls
- Precomputed similarity matrix

to deliver recommendations instantly.

---

### 🌐 Interactive UI

Built with Streamlit to provide

- Clean interface
- Responsive layout
- Easy navigation
- Smooth user experience

---

# 🔍 Recommendation Workflow

```
TMDB Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Tag Generation
      │
      ▼
CountVectorizer
      │
      ▼
Vector Matrix
      │
      ▼
Cosine Similarity
      │
      ▼
Top Similar Movies
      │
      ▼
Streamlit Interface
```

---

# 🛠 Installation

## Clone the repository

```bash
git clone https://github.com/devdhruvsingh/Movie-recommendation-System.git

cd Movie-recommendation-System
```

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure OMDb API

Create a hidden folder

```bash
mkdir .streamlit
```

Create

```
.streamlit/secrets.toml
```

Add your API key

```toml
OMDB_API_KEY = "your_api_key_here"
```

---

## Generate Recommendation Files

Open

```
recommender.ipynb
```

Run every notebook cell to generate

- `movie_dict.pkl`
- `similarity.pkl`

---

## Launch the Application

```bash
streamlit run app.py
```

---

# 📊 Future Improvements

- ⭐ Collaborative Filtering
- 🤖 Deep Learning Recommendation Engine
- ❤️ User Login & Personal Watchlist
- 🎭 Mood-Based Movie Recommendations
- 🎥 Trailer Integration
- 🔍 Advanced Search & Filters
- 📱 Mobile Responsive Design
- ☁️ Cloud Database Integration

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve CineMatch AI:

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project while retaining the original license.

---

# 👨‍💻 Author

### **Dhruv Singh**

**Data Scientist | Product Manager | Machine Learning Enthusiast**

- GitHub: https://github.com/devdhruvsingh
- LinkedIn: *(Add your LinkedIn profile)*
- Portfolio: *(Add your portfolio website if available)*

---

## ⭐ If you found this project useful, don't forget to star the repository!

Your support motivates further improvements and more open-source projects.
