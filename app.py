import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'your_api_key'
tmdb.language = 'ko-KR' # 한국어 기준 데이터 불러오기

def get_recommendations(title):
    idx = movies[movies['title'] == title].index[0]
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    
    movie_indices = [i[0] for i in sim_scores]
    
    images = []
    titles = []
    for i in movie_indices:
        id = movies['id'].iloc[i]
        details = movie.details(id) # id 변수를 통해 TMDb로부터 영화 세부 정보(예산, 홈페이지, 언어 등)를 받아옵니다.
        
        image_path = details['poster_path']
        if image_path:
            image_path = 'https://image.tmdb.org/t/p/w500' + image_path
        else:
            image_path = 'no_image.jpg'
        images.append(image_path)
        titles.append(details['title'])
    
    return images, titles

movies = pickle.load(open('movies.pickle', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle', 'rb'))

st.set_page_config(layout='wide')
st.header('JKDb')

movie_list = movies['title'].values
title = st.selectbox('Choose a movie you like below!', movie_list)
if st.button('Recommend'):
    with st.spinner('Please wait until the process is done...'):
        images, titles = get_recommendations(title)
        
        idx = 0
        for i in range(0, 2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1