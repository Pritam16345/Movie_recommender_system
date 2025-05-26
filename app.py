import streamlit as st
import pickle
import pandas as pd

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        title = movies.iloc[i[0]].title
        movie_id = movies.iloc[i[0]].movie_id
        link = f"https://www.themoviedb.org/movie/{movie_id}"
        recommended_movies.append((title, link))

    return recommended_movies

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Search for a movie you like:',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")

    for title, link in recommendations:
        st.markdown(f"[{title}]({link})", unsafe_allow_html=True)
