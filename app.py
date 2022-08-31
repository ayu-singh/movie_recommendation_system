import streamlit as st
import json
import requests

with open("data/recommendations.json", "r") as fp:
    recommendations = json.load(fp)

movie2id = {dic["name"]: k for k, dic in recommendations.items()}
movies_list = [dic["name"] for movie_id, dic in recommendations.items()]
# print(movie2id)


def get_poster_path(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=49a18fb4b02ce5e9a63cacb96f8f63f6&language=en-US")
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


st.title("Movie Recommender System")
selected_movie = st.selectbox(
    "These are the list of movies available with us, Select One",
    movies_list)

if st.button("Recommend"):
    need_rec_for = movie2id[selected_movie]
    recomendor_output = recommendations[need_rec_for]["recommendations"]
    rec_movie_posters = [get_poster_path(movie2id[rec_name]) for rec_name in recomendor_output]
    # for movie_name in recomendor_output:
    #     st.write(movie_name)
    num_rec = len(recomendor_output)
    containers = st.columns(num_rec)
    for col, rec_movie_name, poster in zip(containers, recomendor_output, rec_movie_posters):
        with col:
            st.text(f"{rec_movie_name}")
            st.image(poster)