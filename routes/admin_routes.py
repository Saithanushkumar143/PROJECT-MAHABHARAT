from flask import Blueprint, render_template, request, redirect, url_for, session
from insert_wisdom import collection

admin_routes = Blueprint('admin_routes', __name__)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'wisdom123'

@admin_routes.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_routes.admin_panel'))
        return "Invalid credentials"

    return render_template('admin_login.html')

@admin_routes.route('/admin')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))

    return render_template('admin_panel.html')

@admin_routes.route('/admin/add_wisdom', methods=['POST'])
def add_wisdom():
    if not session.get('admin_logged_in'):
        return "Unauthorized", 403

    data = {
        "scenario": request.form.get('scenario'),
        "category": request.form.get('category'),
        "characters": request.form.get('characters'),
        "lesson": request.form.get('lesson'),
        "shloka": request.form.get('shloka')
    }
    collection.insert_one(data)
    return redirect(url_for('admin_routes.admin_panel'))
