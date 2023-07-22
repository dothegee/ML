# pip install streamlit
# 데이터사이언스관련 내용을 웹에서 볼수 있게 하기 위해
# pip install tmdbv3api
# tmdb5000을 검색해서 데이터 다운했는데 api를 따와서 하기 위해

# 실행 시킬때 터미널에 streamlit run 영화추천웹사이트.py

import pickle
import streamlit as st
from tmdbv3api import Movie, TMDb

movie = Movie()
tmdb = TMDb()
tmdb.api_key = 'API 키 값 입력하기' # tmdb 웹사이트에서 api 키 가져오기
# 한국어로 설정
tmdb.language = 'ko-KR'
def get_recommendations(title):
    # 영화 제목을 통해서 전체 데이터 기준 그 영화의 index 값 얻기 (.index는 배열로 넘어오기 때문에 [0] 붙이기)
    idx = movies[movies['title']==title].index[0]
    # 코사인 유사도 매트릭스에서 idx에 해당하는 데이터를 (idx, 유사도) 형태로 얻기
    sim = list(enumerate(cosine_sim[idx]))
    
    sim = sorted(sim, key = lambda x: x[1], reverse=True)
    # 자기 자신을 제외한 10개의 추천 영화를 슬라이싱
    sim = sim[1:11]
    # 추천 영화 목록 10개의 인덱스 
    title_list = []
    image_list = []
    movie_indice = [i[0] for i in sim]
    for i in movie_indice:
        id = movies['id'].iloc[i]
        details = movie.details(id)
        # print(details)
        poster_path = details["poster_path"]
        if poster_path:

# tmdb movies detail 구글 검색
            image_list.append(f'https://image.tmdb.org/t/p/w500{details["poster_path"]}')
        else:
            image_list.append('no_image.jpg')
        title_list.append(details['title'])
    return image_list, title_list


movies = pickle.load(open('movies.pickle','rb'))
cosine_sim = pickle.load(open('cosine_sim.pickle','rb'))

st.set_page_config(layout='wide') # 전체화면을 위해 layout = 'wide'
st.header('DOOTHEGEE')

movie_list = movies['title'].values
title = st.selectbox('choose a movie you like', movie_list) # 박스 만들기
# 선택된 영화를 title이라는 변수로 지정

if st.button('Recommend'):
    # 버튼을 눌렀을 때 loading 표시
    with st.spinner('PLZ WAIT!!!!!!!!!!!!!!!!!!!!!!'):
        images, titles = get_recommendations(title)
        # 두줄로 다섯개씩 10개의 데이터를 표시

        idx = 0
        for i in range(0,2):
            cols = st.columns(5)
            for col in cols:
                col.image(images[idx])
                col.write(titles[idx])
                idx += 1
