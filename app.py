from flask import Flask, render_template, redirect, url_for, request, jsonify
from routes import login_routes, dashboard_routes, wisdom_routes
from routes.admin_routes import admin_routes
from pymongo import MongoClient
import os
import re
import traceback
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

# --- Flask App Setup ---
app = Flask(__name__)
app.secret_key = '8b28c742ea3a493d97bfb5f705e6ef61b19d2231'  # Change this in production

# --- MongoDB Atlas Setup ---
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['kurukshetramind']
pravachanas_collection = db['pravachanas']

# --- Register Blueprints ---
app.register_blueprint(login_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(wisdom_routes)
app.register_blueprint(admin_routes, url_prefix='/admin')

# --- YouTube Video ID Extractor ---
def extract_video_id(link):
    match = re.search(r'(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})', link)
    return match.group(1) if match else None

app.jinja_env.filters['extract_youtube_id'] = extract_video_id

# --- Routes ---

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

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
        videos = list(pravachanas_collection.find())
        return render_template('pravachanas.html', pravachanas=videos)
    except Exception as e:
        print(f"[ERROR loading Pravachanas]: {e}")
        return render_template('pravachanas.html', pravachanas=[])

@app.route('/admin_pravachanas')
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
        videos = list(pravachanas_collection.find({"feeling": {"$exists": True}}))
        return render_template('feeling_manager.html', pravachanas=videos)
    except Exception as e:
        print(f"[ERROR loading Feeling Manager Pravachanas]: {e}")
        return render_template('feeling_manager.html', pravachanas=[])

@app.route('/api/submit-pravachanas', methods=['POST'])
def submit_pravachanas():
    try:
        data = request.get_json(force=True)
        youtube_link = data.get('youtube_link', '').strip()
        category = data.get('category', '').strip()
        author = data.get('author', '').strip()
        feeling = data.get('feeling') or data.get('feeling-type') or data.get('feeling_type')

        if not youtube_link or not category or not author or not feeling:
            return jsonify({'success': False, 'error': 'All fields are required'}), 400

        video_id = extract_video_id(youtube_link)
        if not video_id:
            return jsonify({'success': False, 'error': 'Invalid YouTube link format'}), 400

        pravachana_doc = {
            'video_id': video_id,
            'youtube_link': youtube_link,
            'category': category,
            'author': author,
            'feeling': feeling
        }

        result = pravachanas_collection.insert_one(pravachana_doc)
        return jsonify({'success': True, 'id': str(result.inserted_id)})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'success': False, 'error': 'Failed to submit'}), 500

# --- Server Run ---
if __name__ == '__main__':
    app.run(debug=True)
