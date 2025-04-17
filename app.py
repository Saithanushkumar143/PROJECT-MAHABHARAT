from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import fuzz  # Added for better matching
import numpy as np

# Flask App
app = Flask(__name__)
from flask_cors import CORS

CORS(app)  # Enables CORS for all routes

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["MahabharataWisdom"]
collection = db["wisdom"]

# Function to fetch wisdom from MongoDB
def fetch_wisdom():
    wisdom_data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ID
    return wisdom_data

# Function to get the most relevant wisdom based on similarity
def get_best_wisdom(user_input, wisdom_data):
    documents = [item["scenario"] for item in wisdom_data]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    doc_vectors = vectorizer.fit_transform(documents)
    user_vector = vectorizer.transform([user_input])

    # Compute cosine similarity
    similarity_scores = cosine_similarity(user_vector, doc_vectors).flatten()

    # 🔥 Fallback with Fuzzy Matching
    fuzz_matches = [fuzz.partial_ratio(user_input, doc) for doc in documents]

    # 🔥 Use both Cosine Similarity and Fuzzy Matching
    combined_scores = np.array(similarity_scores) * 0.7 + np.array(fuzz_matches) * 0.3

    best_score = np.max(combined_scores)
    best_match_index = np.argmax(combined_scores)

    # 💡 Lower threshold for better matches
    if best_score > 0.01:  
        best_match = wisdom_data[best_match_index]

        # ✅ Fix serialization issue
        response = {
            "category": best_match["category"],
            "scenario": best_match["scenario"],
            "characters": best_match["characters"],
            "lesson": best_match["lesson"],
            "shloka": best_match.get("shloka", "No shloka available"),
            "similarity_score": float(best_score)  # Convert float32 to Python float
        }
        return response
    else:
        return {"error": "No relevant wisdom found. Try a different query."}

# Flask Route for UI
@app.route('/')
def home():
    return render_template('index.html')

# Flask Route for Wisdom Retrieval
@app.route('/get_wisdom', methods=['GET'])
def get_wisdom():
    user_input = request.args.get('query', '')

    if not user_input:
        return jsonify({"error": "No query provided."})

    # Fetch wisdom from MongoDB
    wisdom_data = fetch_wisdom()

    # Get the best wisdom match
    response = get_best_wisdom(user_input, wisdom_data)

    # Return the result as JSON
    return jsonify(response)

# Flask App Execution
if __name__ == '__main__':
    app.run(debug=True)
