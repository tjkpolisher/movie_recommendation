import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = '3019e801586007686815678fcc93089f'

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('JKDb')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like below!', movie_list)
if st.button('Recommend'):
    pass