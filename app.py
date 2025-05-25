from flask import Flask, render_template, redirect, url_for, request, jsonify
from routes import login_routes, dashboard_routes, wisdom_routes
from routes.admin_routes import admin_routes
from pymongo import MongoClient
import re
import traceback

# --- Flask App Setup ---
app = Flask(__name__)
app.secret_key = '8b28c742ea3a493d97bfb5f705e6ef61b19d2231'  # Replace this with a secure value in production

# --- MongoDB Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client['kurukshetramind']
pravachanas_collection = db['pravachanas']

# --- Register Blueprints ---
app.register_blueprint(login_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(wisdom_routes)
app.register_blueprint(admin_routes, url_prefix='/admin')

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

# Make the extractor available in Jinja templates
app.jinja_env.filters['extract_youtube_id'] = extract_video_id

# --- Routes ---

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/user_menu')
def user_menu():
    return redirect(url_for('dashboard_routes.dashboard'))

@app.route('/admin_menu')
def admin_menu():
    return redirect(url_for('admin_routes.admin_login'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/pravachanas')
def pravachanas():
    try:
        # Show all videos, regardless of 'feeling' field
        videos = list(pravachanas_collection.find())
        return render_template('pravachanas.html', pravachanas=videos)
    except Exception as e:
        print(f"[ERROR loading Pravachanas]: {e}")
        return render_template('pravachanas.html', pravachanas=[])

@app.route('/admin/pravachanas')
def admin_pravachanas():
    try:
        videos = list(pravachanas_collection.find())
        return render_template('admin_pravachanas.html', pravachanas=videos)
    except Exception as e:
        print(f"[ERROR loading Admin Pravachanas]: {e}")
        return render_template('admin_pravachanas.html', pravachanas=[])

@app.route('/feeling_manager')
def feeling_manager():
    try:
        # Fetch all pravachanas that have a 'feeling' field
        videos = list(pravachanas_collection.find({"feeling": {"$exists": True}}))
        return render_template('feeling_manager.html', pravachanas=videos)
    except Exception as e:
        print(f"[ERROR loading Feeling Manager Pravachanas]: {e}")
        return render_template('feeling_manager.html', pravachanas=[])

@app.route('/api/submit-pravachanas', methods=['POST'])
def submit_pravachanas():
    try:
        data = request.get_json(force=True)

        print(f"[DEBUG] Raw request JSON: {data}")

        youtube_link = data.get('youtube_link', '').strip()
        category = data.get('category', '').strip()
        author = data.get('author', '').strip()
        # Accept all possible keys for feeling
        feeling = data.get('feeling') or data.get('feeling-type') or data.get('feeling_type')

        print(f"[DEBUG] youtube_link: {youtube_link}")
        print(f"[DEBUG] category: {category}")
        print(f"[DEBUG] author: {author}")
        print(f"[DEBUG] feeling: {feeling}")

        if not youtube_link or not category or not author or not feeling:
            print("[ERROR] One or more required fields are missing.")
            return jsonify({'success': False, 'error': 'All fields are required'}), 400

        video_id = extract_video_id(youtube_link)
        print(f"[DEBUG] Extracted video_id: {video_id}")

        if not video_id:
            print("[ERROR] Invalid YouTube link.")
            return jsonify({'success': False, 'error': 'Invalid YouTube link format'}), 400

        pravachana_doc = {
            'video_id': video_id,
            'youtube_link': youtube_link,
            'category': category,
            'author': author,
            'feeling': feeling  # always use 'feeling'
        }

        result = pravachanas_collection.insert_one(pravachana_doc)
        print(f"[DEBUG] Successfully inserted with ID: {result.inserted_id}")

        return jsonify({'success': True})

    except Exception as e:
        print("[ERROR] Exception occurred during Pravachana submission.")
        traceback.print_exc()
        return jsonify({'success': False, 'error': 'Failed to submit'}), 500

# --- Run Server ---
if __name__ == '__main__':
    app.run(debug=True)
