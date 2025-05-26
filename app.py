import streamlit as st
import pickle
import requests

api_key = "7cd2b0b1222b30ddc1b124bd131e5ca1"

movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"

    except Exception as e:
        return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movies = []
    rec_posters = []
    rec_links = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster = fetch_poster(movie_id)
        link = f"https://www.themoviedb.org/movie/{movie_id}"

        rec_movies.append(title)
        rec_posters.append(poster)
        rec_links.append(link)

    return rec_movies, rec_posters, rec_links

st.title('🎬 Movie Recommender System')

selected_movie = st.selectbox(
    'Search for a movie you like:',
    movies['title'].values)

if st.button('Recommend'):
    titles, posters, links = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            if posters[i]:
                st.image(posters[i], use_container_width=True)
            else:
                st.image("https://via.placeholder.com/300x450?text=No+Image", use_container_width=True)
            st.markdown(f"[{titles[i]}]({links[i]})", unsafe_allow_html=True)
