import streamlit as st
import pandas as pd

# ---------- Load Data ----------
@st.cache_data
def load_data():
    return pd.read_csv("movies.csv")

df = load_data()

# ---------- Page Setup ----------
st.set_page_config(page_title="Movie Recommender", page_icon="🎬")
st.title("🎬 Movie Recommender")
st.write("Pick your mood and genre, and I'll suggest a movie for you!")

# ---------- User Inputs ----------
genres = sorted(df["genre"].unique())
moods = sorted(df["mood"].unique())

selected_genre = st.selectbox("Choose a genre:", genres)
selected_mood = st.selectbox("Choose a mood:", moods)
min_rating = st.slider("Minimum rating:", 6.0, 9.0, 7.0, 0.1)

# ---------- Recommendation Logic ----------
def recommend_movies(data, genre, mood, min_rating):
    filtered = data[
        (data["genre"] == genre) &
        (data["mood"] == mood) &
        (data["rating"] >= min_rating)
    ]
    return filtered.sort_values(by="rating", ascending=False)

if st.button("Recommend me a movie 🎥"):
    results = recommend_movies(df, selected_genre, selected_mood, min_rating)

    if not results.empty:
        st.success(f"Found {len(results)} movie(s) for you:")
        for _, row in results.iterrows():
            st.markdown(f"**{row['title']}** ({row['year']}) — ⭐ {row['rating']}")
    else:
        st.warning("No exact match found. Try changing genre, mood, or lowering the rating.")

st.markdown("---")
st.caption("Mini project: built with Streamlit + Pandas | Learning project by an AI&DS student")
