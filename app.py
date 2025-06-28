import streamlit as st
import pickle
import pandas as pd
import requests 

st.title('Movie Recommender System')
your_api_key = 'your_api_key_here'
# Load data
movies = pd.read_csv('movies.csv')
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_data(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={your_api_key}&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get("poster_path", None)
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie {movie_id}: {e}")
        return "https://via.placeholder.com/500x750?text=Error"

def recommend_movie(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:30]
    
    recommended_movie_poster = []
    recommended_movie_name = []
    
    for i in movie_list:
        recommended_movie_name.append(movies.iloc[i[0]]['title'])
        recommended_movie_poster.append(fetch_data(movies.iloc[i[0]]['movie_id']))
    
    return recommended_movie_name, recommended_movie_poster

# Dropdown
selected_movie_name = st.selectbox("Which movie are you looking for?", movies['title'])

# Button
if st.button("Recommend"):
    st.write("You selected:", selected_movie_name)
    names, posters = recommend_movie(selected_movie_name)

    # Loop through recommendations in chunks of 3
    for i in range(0, len(names), 3):
        cols = st.columns(3)  # Create 3 columns

        for j in range(3):
            if i + j < len(names):
                with cols[j]:
                    st.image(posters[i + j])
                    st.caption(names[i + j])

