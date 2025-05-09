from flask import Blueprint, render_template, request, redirect, url_for, session

login_routes = Blueprint('login', __name__)

# Dummy user for testing (you can replace this with real auth logic)
users = {"admin": "password123"}

@login_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('dashboard_routes.dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')


@login_routes.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login.login'))
