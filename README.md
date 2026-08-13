# 🎬 Movie Recommender (Mini Project)

A simple rule-based movie recommender built with Python, Pandas, and Streamlit.
Built as a learning project to practice the full cycle: code → run → deploy.

## What it does
You pick a genre, mood, and minimum rating — the app filters a small movie
dataset (`movies.csv`) and recommends matching movies.

## Files
- `app.py` — the Streamlit app (UI + logic)
- `movies.csv` — the dataset (20 movies with genre, mood, rating, year)
- `requirements.txt` — Python packages needed

## Part 1: Run it on your own computer

1. **Install Python** (3.9+) if you don't have it: https://www.python.org/downloads/

2. **Open a terminal/command prompt** in this project folder.

3. **(Recommended) Create a virtual environment:**
   ```
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install the requirements:**
   ```
   pip install -r requirements.txt
   ```

5. **Run the app:**
   ```
   streamlit run app.py
   ```
   Your browser should open automatically at `http://localhost:8501`.
   If not, copy that link into your browser manually.

6. Play with the dropdowns and click "Recommend me a movie 🎥" — you should see
   results appear.

## Part 2: Push it to GitHub

1. Create a free account at https://github.com if you don't have one.
2. Create a new repository, e.g. `movie-recommender`.
3. In your project folder, run:
   ```
   git init
   git add .
   git commit -m "First version of movie recommender"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/movie-recommender.git
   git push -u origin main
   ```
   (Replace `YOUR_USERNAME` with your GitHub username.)

## Part 3: Deploy for free on Streamlit Community Cloud

1. Go to https://share.streamlit.io and sign in with your GitHub account.
2. Click "New app".
3. Select your `movie-recommender` repository, branch `main`, and file `app.py`.
4. Click "Deploy". Wait 1-2 minutes.
5. You'll get a public shareable link like:
   `https://your-app-name.streamlit.app`

That's it — you now have a live, working, deployed AI/DS mini project you can
put on your resume or show in college.

## Ideas to extend it later (optional, once comfortable)
- Add more movies to `movies.csv`
- Add a poster image column and display images
- Replace the rule-based filter with a simple ML model (e.g., KNN using
  genre/mood/rating as features)
- Add a search bar to look up a movie by name
