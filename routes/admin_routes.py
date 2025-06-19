from flask import Blueprint, render_template, request, redirect, url_for, session
from pymongo import MongoClient
from bson.objectid import ObjectId
import re
import os
from dotenv import load_dotenv
load_dotenv()


admin_routes = Blueprint('admin_routes', __name__)

# --- MongoDB Setup ---
client = MongoClient("mongodb+srv://kurukshetramind:myfirstproject123@cluster0.lqecbti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['kurukshetramind']
pravachanas_collection = db['pravachanas']

# --- Admin Credentials ---
import os
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')


# --- Admin Login ---
@admin_routes.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_routes.admin_panel'))

        return render_template('admin_login.html', error="Invalid credentials")
    
    return render_template('admin_login.html')

# --- Admin Panel Dashboard ---
@admin_routes.route('/panel')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))
    
    return render_template('admin_panel.html')

# --- View All Pravachanas (Admin) ---
@admin_routes.route('/pravachanas')
def admin_pravachanas():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))

    videos = list(pravachanas_collection.find())
    return render_template('admin_pravachanas.html', pravachanas=videos)

# --- Submit Pravachanas via Form (Reliable Upload Method) ---
@admin_routes.route('/submit-pravachanas-form', methods=['POST'])
def submit_pravachanas_form():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))

    try:
        youtube_link = request.form.get('youtube_link', '').strip()
        category = request.form.get('category', '').strip()
        author = request.form.get('author', '').strip()
        feeling = request.form.get('feeling', '').strip()

        # Extract YouTube video ID
        match = re.search(r'(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})', youtube_link)
        video_id = match.group(1) if match else None

        if not youtube_link or not category or not author or not feeling or not video_id:
            error_msg = "All fields are required and YouTube link must be valid."
            return render_template('admin_pravachanas.html', pravachanas=list(pravachanas_collection.find()), error=error_msg)

        pravachana_doc = {
            'video_id': video_id,
            'youtube_link': youtube_link,
            'category': category,
            'author': author,
            'feeling': feeling
        }

        pravachanas_collection.insert_one(pravachana_doc)
        return redirect(url_for('admin_routes.admin_pravachanas'))

    except Exception as e:
        print("[ERROR submitting Pravachana via form]:", e)
        return render_template('admin_pravachanas.html', pravachanas=list(pravachanas_collection.find()), error="Internal error occurred.")

# --- Delete Pravachana ---
@admin_routes.route('/delete_video/<video_id>', methods=['POST'])
def delete_video(video_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))

    pravachanas_collection.delete_one({'_id': ObjectId(video_id)})
    return redirect(url_for('admin_routes.admin_pravachanas'))

# --- Edit Pravachana ---
@admin_routes.route('/edit_video/<video_id>', methods=['POST'])
def edit_video(video_id):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))

    new_link = request.form.get('youtube_link', '').strip()
    new_category = request.form.get('category', '').strip()
    new_author = request.form.get('author', '').strip()

    # Extract YouTube video ID
    match = re.search(r'(?:v=|youtu\.be/|embed/)([a-zA-Z0-9_-]{11})', new_link)
    video_id_only = match.group(1) if match else None

    update_data = {
        'category': new_category,
        'author': new_author
    }

    if video_id_only:
        update_data['video_id'] = video_id_only
        update_data['youtube_link'] = new_link

    pravachanas_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': update_data}
    )

    return redirect(url_for('admin_routes.admin_pravachanas'))
