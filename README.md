# 🎬 MoviesNow — Smart Movie Recommender
### Artificial Intelligence Project · 90 Hours

> A web-based AI application that recommends movies using **Content-Based Filtering**
> (TF-IDF Vectorisation + Cosine Similarity), built end-to-end with Python and Flask.

---

## 📁 Project Structure

```
movie-recommender/
│
├── app.py                  ← Flask web server & REST API routes
├── recommender.py          ← Core ML model (TF-IDF + Cosine Similarity)
├── movies.csv              ← Dataset  ← YOU MUST DOWNLOAD THIS
├── requirements.txt        ← Python dependencies
│
├── templates/
│   └── index.html          ← Full frontend (HTML + CSS + JS, single file)
│
└── README.md               ← This file
```

---

## ⚙️ Setup — Step by Step

### Step 1 — Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2 — Download the Dataset
1. Visit: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata
2. Download `tmdb_5000_movies.csv`
3. **Rename it to `movies.csv`**
4. Place it in the project root (same folder as `app.py`)

### Step 3 — Run the App
```bash
python app.py
```

### Step 4 — Open in Your Browser
```
http://127.0.0.1:5000
```

---

## 🧠 ML Pipeline Explained

```
Raw CSV
  │
  ▼
[1] Load & Select Columns
    pandas.read_csv() → title, overview, genres, keywords, vote_average, release_date
  │
  ▼
[2] Preprocess
    - Parse genres / keywords (JSON string → plain text)
    - Fill NaN values
    - Concatenate: genres + keywords + overview → "combined" text per movie
  │
  ▼
[3] TF-IDF Vectorisation
    TfidfVectorizer(max_features=15000, ngram_range=(1,2), stop_words='english')
    → sparse matrix  shape: (5000, 15000)
  │
  ▼
[4] Cosine Similarity Matrix
    cosine_similarity(matrix, matrix)
    → dense matrix  shape: (5000, 5000)
    Built ONCE at startup; reused for all queries.
  │
  ▼
[5] Query
    User types "Inception"
    → look up row index → sort by similarity score → return top-8
  │
  ▼
[6] Flask REST API  →  JSON response  →  Rendered in browser
```

---

## 📡 API Endpoints

| Method | Route          | Description                         |
|--------|---------------|-------------------------------------|
| GET    | `/`            | Main web UI                         |
| POST   | `/recommend`   | Body: `{"title":"..."}` → JSON recs |
| GET    | `/search?q=..` | Autocomplete title list             |
| GET    | `/stats`       | Dataset statistics                  |
| GET    | `/health`      | Server + model status               |

---

## 🎓 Learning Outcomes Covered (90 Hours)

| Topic                          | Where Applied              |
|-------------------------------|---------------------------|
| Python programming            | All files                  |
| Data loading & preprocessing  | `recommender.py` Step 1–2  |
| Feature engineering           | `recommender.py` Step 2    |
| TF-IDF vectorisation          | `recommender.py` Step 3    |
| Cosine similarity (ML)        | `recommender.py` Step 4    |
| Content-based filtering       | `recommender.py` Step 5    |
| REST API design               | `app.py`                   |
| Web deployment with Flask     | `app.py`                   |
| Frontend (HTML/CSS/JS)        | `templates/index.html`     |
| End-to-end AI/ML lifecycle    | Entire project             |

---

## 🔧 Troubleshooting

| Problem                      | Fix                                                      |
|-----------------------------|----------------------------------------------------------|
| "Dataset not found"          | Check that `movies.csv` is in the project root folder    |
| First load is slow (~15s)    | Normal — building the similarity matrix takes a moment   |
| Movie not found              | Try a more popular title; the dataset has ~5,000 films   |
| Port 5000 already in use     | Change `port=5000` to `port=5001` in `app.py`            |

---

## 📦 Dependencies

```
flask>=2.3.0        Web server framework
pandas>=2.0.0       Data loading and manipulation
numpy>=1.24.0       Numerical computing
scikit-learn>=1.3.0 TF-IDF + Cosine Similarity
```
