from flask import Blueprint, render_template, request, session
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz
import numpy as np

dashboard_routes = Blueprint('dashboard_routes', __name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["MahabharataWisdom"]
collection = db["wisdom"]

# Fetch wisdom data
def fetch_wisdom():
    return list(collection.find({}, {"_id": 0}))

# Match user input to best wisdom
def get_best_wisdom(user_input, wisdom_data):
    documents = [item["scenario"] for item in wisdom_data]
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    user_vector = vectorizer.transform([user_input])

    cosine_scores = cosine_similarity(user_vector, doc_vectors).flatten()
    fuzz_scores = [fuzz.partial_ratio(user_input, doc) for doc in documents]

    combined_scores = np.array(cosine_scores) * 0.7 + np.array(fuzz_scores) * 0.3
    best_index = np.argmax(combined_scores)
    best_score = np.max(combined_scores)

    if best_score > 0.01:
        best_match = wisdom_data[best_index]
        return {
            "category": best_match["category"],
            "scenario": best_match["scenario"],
            "characters": best_match["characters"],
            "lesson": best_match["lesson"],
            "shloka": best_match.get("shloka", "No shloka available"),
            "similarity_score": float(best_score)
        }
    else:
        return None

@dashboard_routes.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    wisdom_result = None

    if request.method == 'POST':
        query = request.form.get('query')
        wisdom_data = fetch_wisdom()
        wisdom_result = get_best_wisdom(query, wisdom_data)

    username = session.get('username', 'Guest')
    return render_template('dashboard.html', username=username, result=wisdom_result)
