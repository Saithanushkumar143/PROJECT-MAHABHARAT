from flask import Blueprint, render_template, request, redirect, url_for, session
from insert_wisdom import collection

admin_routes = Blueprint('admin_routes', __name__)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'wisdom123'

@admin_routes.route('/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin_routes.admin_panel'))
        
        # ❗ Return the template with the error instead of plain text
        return render_template('admin_login.html', error="Invalid credentials")

    return render_template('admin_login.html')

@admin_routes.route('/panel')
def admin_panel():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_routes.admin_login'))
    
    return render_template('admin_panel.html')
