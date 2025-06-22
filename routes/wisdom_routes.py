from flask import Blueprint, request, jsonify
from pymongo import MongoClient
import re
import os
# --- MongoDB Setup ---
# client = MongoClient("mongodb+srv://kurukshetramind:myfirstproject123@cluster0.lqecbti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# client = MongoClient("mongodb://localhost:27017/")
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['kurukshetramind']
collection = db['wisdom']

# --- Blueprint Setup ---
wisdom_routes = Blueprint('wisdom_routes', __name__)

# --- YouTube Video ID Extractor ---
def extract_video_id(link):
    """
    Extracts the YouTube video ID from common URL formats.
    Supports:
    - https://www.youtube.com/watch?v=VIDEO_ID
    - https://youtu.be/VIDEO_ID
    - https://www.youtube.com/embed/VIDEO_ID
    """
    match = re.search(r'(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})', link)
    return match.group(1) if match else None

# --- Routes ---

@wisdom_routes.route('/get_wisdom')
def get_wisdom():
    query = request.args.get('query', '').strip()

    # Basic validation
    if not query:
        return jsonify({"error": "Empty query"}), 400

    # For now, let's just return the query as the lesson
    lesson = query
    shloka = "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।"  # Default shloka
    response = ""

    # Find a matching wisdom entry
    wisdom_entry = collection.find_one({"$text": {"$search": query}})

    if wisdom_entry:
        lesson = wisdom_entry.get("lesson", lesson)
        shloka = wisdom_entry.get("shloka", shloka)
        response = wisdom_entry.get("response", "")

    return jsonify({
        "lesson": lesson or "No lesson found.",
        "shloka": shloka or "No shloka available.",
        "response": response or "No response available."
    })