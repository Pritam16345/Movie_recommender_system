🎬 Movie Recommender System

This is a simple and effective Content-Based Movie Recommender System built using Python and Streamlit, which allows users to get quick movie recommendations based on the one they select. The system uses cosine similarity on feature vectors and includes direct links to TMDb for each recommended movie.


✨ Features

🔎 Recommends 5 movies similar to the one selected

🧠 Uses content similarity from a precomputed matrix

🌐 Provides clickable links to The Movie Database (TMDb)

🖥️ Interactive and lightweight web app built with Streamlit

🧪 Efficient backend using preprocessed .pkl files for fast response


⚙️ Tech Stack

Frontend: Streamlit

Backend: Python

Libraries: pandas, pickle, streamlit

Data Source: Preprocessed movie metadata + similarity matrix

API Integration: Direct TMDb links for additional info


📦 Files Overview

app.py — Main Streamlit application

movie_dict.pkl — Contains movie titles and TMDb IDs

similarity.pkl — Precomputed similarity matrix for recommendations
