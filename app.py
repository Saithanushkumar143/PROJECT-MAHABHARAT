from flask import Flask, render_template
from routes import login_routes, dashboard_routes, wisdom_routes
from routes.admin_routes import admin_routes  # <-- Register the admin routes

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Keep this secret in production

# Register Blueprints
app.register_blueprint(login_routes)
app.register_blueprint(dashboard_routes)
app.register_blueprint(wisdom_routes)
app.register_blueprint(admin_routes)  # <-- This line is crucial

# Route for Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Route for Signup Page
@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/pravachanas')
def pravachanas():
    return render_template('pravachanas.html')
# Run the app
if __name__ == '__main__':
    app.run(debug=True)
