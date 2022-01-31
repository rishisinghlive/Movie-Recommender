import streamlit as st
import pandas as pd
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8fed6dac8536ee192af4b40ad0ce70ec&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters


movies = pd.read_csv('movie.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender')

selected_movie_name = st.selectbox('The movie you like', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(posters[0])
        st.caption(names[0])
    with col2:
        st.image(posters[1])
        st.caption(names[1])
    with col3:
        st.image(posters[2])
        st.caption(names[2])
    with col4:
        st.image(posters[3])
        st.caption(names[3])
    with col5:
        st.image(posters[4])
        st.caption(names[4])


