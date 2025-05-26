🎬 Movie Recommender System

This is a Content-Based Movie Recommender System built using Python, Streamlit, and The Movie Database (TMDb) API. The app recommends five similar movies based on a user-selected title and displays their posters along with direct links to TMDb for more details.



✅ Features :-

🎥 Recommend top 5 similar movies for any selected title

🖼️ Displays movie posters using TMDb API

🔗 Clickable links to official TMDb movie pages

⚡ Fast and responsive with precomputed similarity matrix

💻 Lightweight web app built with Streamlit



🧠 How It Works :-

Uses a content-based filtering approach

Computes similarity between movies based on feature vectors

Retrieves poster images and movie links from TMDb using the movie ID



🔧 Tech Stack :-

Frontend: Streamlit

Backend: Python

Libraries: pandas, pickle, requests, streamlit

API: TMDb API v3



📦 Project Files :-

app.py – Main Streamlit application script

movies.pkl – Pickled DataFrame containing movie titles and TMDb IDs

similarity.pkl – Precomputed similarity matrix
