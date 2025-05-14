from flask import Flask, render_template, redirect, url_for, session, request, jsonify
from routes import login_routes, dashboard_routes, wisdom_routes
from routes.admin_routes import admin_routes  # Register the admin routes

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Keep this secret in production

# Register Blueprints
app.register_blueprint(login_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(wisdom_routes)
app.register_blueprint(admin_routes, url_prefix='/admin')  # Register admin routes with a prefix

# Route for Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Route for Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Route for User Menu - Directly Redirects to Dashboard
@app.route('/user_menu')
def user_menu():
    # Directly redirect to the KurukshetraMind Dashboard
    return redirect(url_for('dashboard_routes.dashboard'))  # Redirect to dashboard directly

# Route for Admin Menu - Redirects to Admin Login
@app.route('/admin_menu')
def admin_menu():
    return redirect(url_for('admin_routes.admin_login'))  # Redirect to admin login page

# Route for Dashboard Page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Route for Pravachanas Page
@app.route('/pravachanas')
def pravachanas():
    return render_template('pravachanas.html')

# Route for Explore Page
@app.route('/explore')
def explore():
    return render_template('explore.html')

# Admin Login Route
@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')  # Render admin login page

# API route to submit Pravachanas data
@app.route('/api/submit-pravachanas', methods=['POST'])
def submit_pravachanas():
    try:
        # Get the form data sent from the frontend
        data = request.get_json()
        youtube_link = data.get('youtube_link')
        category = data.get('category')
        author = data.get('author')

        # For now, let's print it to the console (or save it to a database)
        print(f"Received Pravachana: YouTube Link: {youtube_link}, Category: {category}, Author: {author}")

        # Respond with success
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False})

if __name__ == '__main__':
    app.run(debug=True)
