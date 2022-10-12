
# Import all the below libraries

import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


# Insert the data

movies_data = pd.read_csv("C:/Users/amany/Desktop/DataScience_Projects/Bollywood Movie Recommendation Model/BollywoodMovieDetail.csv")

# Now Convert Some Column into desired specificaton

def remove_bigbar(x):
    token = str(x).split("|")
    str_without_bigbar = ""
    for pointer in token:
        str_without_bigbar += pointer
    return " ".join(str_without_bigbar.split())

movies_data["genre"] = movies_data["genre"].apply(remove_bigbar)
for i in ["actors","directors"]:
    movies_data[i] = movies_data[i].apply(remove_bigbar)

# Fill NaN values by null string

selected_features = ["title","genre","actors","directors"]
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna(" ")

# Now combine selected feature for recommendation

selected_features =  movies_data["genre"] + " " + movies_data["actors"] + " " + movies_data["directors"]

# Now convert string datatype into numeric by "TfidVectorizer" from sklearn library

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(selected_features)

# Matrics of Movies similarity score

similarity = cosine_similarity(feature_vectors)

# Create a list of movie title from movies_data

list_of_movies_title = movies_data["title"].tolist()

# build Ui with help of Streamlit library

st.title("Movies Recommensation System ")


user_movie = st.text_input("Enter the favourite movie name:")

def get_recommended_movie(user_data):
    find_close_match = difflib.get_close_matches(user_data, list_of_movies_title)
    index_of_user_movie = movies_data[movies_data["title"] == find_close_match[0]].index[0]
    similarity_score = list(enumerate(similarity[index_of_user_movie]))
    sorted_similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    i = 1

    list_recommended_movies = []

    for movie in sorted_similarity_score:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if (i < 21):
            list_recommended_movies.append(title_from_index)
            i += 1
    return list_recommended_movies

movies = ""

if st.button("Search Similar Movies"):
    movies = get_recommended_movie(user_movie)

st.success(movies)








