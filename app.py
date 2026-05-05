"""
app.py
======
Flask web server for the Smart Movie Recommender.
"""

from flask import Flask, jsonify, render_template, request

from recommender import recommender

app = Flask(__name__)


@app.before_request
def _ensure_model_loaded():
    """Load the model lazily on the first request."""
    if not recommender.is_loaded:
        try:
            recommender.load_data()
        except (FileNotFoundError, ValueError) as exc:
            print(f"Dataset load warning: {exc}")


@app.route("/")
def index():
    """Serve the main application page."""
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def get_recommendations():
    """Return recommendations for a movie title."""
    body = request.get_json(silent=True) or {}
    title = body.get("title", "").strip()

    if not title:
        return jsonify({"error": "Please provide a movie title."}), 400

    if not recommender.is_loaded:
        return jsonify(
            {
                "error": (
                    "Dataset not loaded. Add a supported TMDB CSV file to the project "
                    "folder: movies.csv, tmdb_5000_movies.csv, credits.csv, or "
                    "tmdb_5000_credits.csv."
                )
            }
        ), 503

    result = recommender.recommend(title)
    status = 200 if "error" not in result else 404
    return jsonify(result), status


@app.route("/search")
def search():
    """Autocomplete title suggestions."""
    query = request.args.get("q", "").strip()
    if len(query) < 2:
        return jsonify([])
    return jsonify(recommender.search_titles(query, limit=8))


@app.route("/stats")
def stats():
    """Return simple dataset statistics."""
    return jsonify(recommender.stats())


@app.route("/health")
def health():
    """Return app and dataset readiness info."""
    return jsonify(
        {
            "status": "ok",
            "model_loaded": recommender.is_loaded,
            "movie_count": len(recommender.df) if recommender.is_loaded else 0,
            "data_source": recommender.data_source if recommender.is_loaded else "",
            "data_files": recommender.data_files if recommender.is_loaded else [],
        }
    )


if __name__ == "__main__":
    print("\nStarting MoviesNow - Smart Movie Recommender")
    print("Open http://127.0.0.1:5000 in your browser\n")
    app.run(debug=True, host="0.0.0.0", port=5000)
