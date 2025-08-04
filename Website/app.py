import streamlit as st
import joblib
import numpy as np
import pandas as pd
import requests
import os

st.write("""
# Machine Learning Movie Recommender System (ML-MRS)
    Built with ML and ☕, this movie recommender knows your next binge 🎥.
""")

current_dir = os.path.dirname(__file__)

# This are the ML model result
similarity_path = os.path.abspath(os.path.join(current_dir, "..", "Output-data", "similarity.joblib")) 
movies_path     = os.path.abspath(os.path.join(current_dir, "..", "Output-data", "movies.joblib")) 

# If joblib files are missing, run the notebook
if not os.path.exists(similarity_path) or not os.path.exists(movies_path):
    st.warning("🔍 ML results not found. Running the model to generate required data...")

    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor

    with open(os.path.abspath(os.path.join(current_dir, "..", "ML-model", "code.ipynb"))) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': os.path.abspath(os.path.join(current_dir, "..", "ML-model"))}})
    
    st.success("✅ Model run complete! Results are now available.")
else:
    st.info("📦 ML model trained on database is ready.")

similarity  = joblib.load(similarity_path) 

# Movies
movies      = joblib.load(movies_path)

# Number of recommended movies
top_movies_count = 5

# TMDB api key
# tmdb_api_key = ''
# tmdb_key_path = os.path.abspath(os.path.join(current_dir, "..", "keys", "tmdb.key"))
# with open(tmdb_key_path) as key_file:
#     tmdb_api_key = key_file.readline()

tmdb_api_key = os.getenv("TMDB_API_KEY")
if tmdb_api_key is None:
    raise ValueError("TMDB_API_KEY environment variable not set")

# Recommend top 5 movies based on the similarity
def recommend(movie):
    movie_index      = movies[movies['title'] == movie].index[0]
    distances        = similarity[movie_index]
    movie_list       = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:top_movies_count + 1]
    return [df_index for df_index, cosine_similarity_value in movie_list]

def fetch_poster(movie_id):
    url         = "https://api.themoviedb.org/3/movie/" + str(movie_id) + "?api_key=" + tmdb_api_key + "&language=en-US"
    response    = requests.get(url)

    if response.status_code != 200:
        st.write("Requests are failing, response code:", response.status_code)
    else:
        data    = response.json()
        relative_poster_path = data['poster_path']
        complete_poster_path = "https://image.tmdb.org/t/p/original" + relative_poster_path
        return complete_poster_path
    
selected_movie_title = st.selectbox("Search for your favorite movie", movies['title'])

if st.button('Search'):
    st.write("Selected Movie:", selected_movie_title)

    single_column                       = st.columns(1)[0]
    with single_column:
        movie_id                        = movies[movies['title'] == selected_movie_title]['id'].iloc[0]
        poster                          = fetch_poster(movie_id)

        # Wrap both image and title in a centered div
        st.markdown(
            f"""
            <div style='text-align: center;'>
                <img src="{poster}" width="200"><br>
                <div style='font-weight: bold; font-size: 18px; margin-top: 10px;'>{selected_movie_title}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("Movies you may like 🩷")
    recommended_movies_df_indices = recommend(selected_movie_title)
    cols = st.columns(top_movies_count)

    for i in range(top_movies_count):
        with cols[i]:
            movie_name = movies.iloc[recommended_movies_df_indices[i]]['title']
            movie_id = movies.iloc[recommended_movies_df_indices[i]]['id']
            poster = fetch_poster(movie_id)

            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <img src="{poster}" width="200"><br>
                    <div style='font-weight: bold; font-size: 18px; margin-top: 10px;'>{movie_name}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
