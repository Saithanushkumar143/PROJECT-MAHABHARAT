from flask import Blueprint, request, jsonify, render_template
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz
import numpy as np

# Blueprint definition
wisdom_routes = Blueprint('wisdom_routes', __name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["kurukshetramind"]
collection = db["wisdom"]

# Fetch all wisdom entries
def fetch_wisdom():
    wisdom_data = list(collection.find({}, {"_id": 0}))
    return wisdom_data

# Compute best matching wisdom entry
def get_best_wisdom(user_input, wisdom_data):
    documents = [item["scenario"] for item in wisdom_data]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    user_vector = vectorizer.transform([user_input])

    # Cosine similarity
    similarity_scores = cosine_similarity(user_vector, doc_vectors).flatten()

    # Fuzzy Matching
    fuzz_scores = [fuzz.partial_ratio(user_input.lower(), doc.lower()) for doc in documents]

    # Combine scores
    combined_scores = np.array(similarity_scores) * 0.7 + np.array(fuzz_scores) * 0.3

    best_score = np.max(combined_scores)
    best_match_index = np.argmax(combined_scores)

    if best_score > 0.01:
        best_match = wisdom_data[best_match_index]
        return {
            "category": best_match["category"],
            "scenario": best_match["scenario"],
            "characters": best_match["characters"],
            "lesson": best_match["lesson"],
            "shloka": best_match.get("shloka", "No shloka available"),
            "similarity_score": float(best_score)
        }
    else:
        return {"error": "No relevant wisdom found. Try a different query."}

# UI route
@wisdom_routes.route('/wisdom')
def wisdom_ui():
    return render_template("wisdom.html")

# API route that handles both GET and POST
@wisdom_routes.route('/get_wisdom', methods=['GET', 'POST'])
def get_wisdom():
    if request.method == 'POST':
        user_input = request.form.get("query", "")
    else:
        user_input = request.args.get("query", "")

    if not user_input:
        return jsonify({"error": "No query provided."})

    wisdom_data = fetch_wisdom()
    result = get_best_wisdom(user_input, wisdom_data)
    return jsonify(result)
