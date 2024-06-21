from flask import Blueprint, request, jsonify, render_template
from backend.models import User
from backend import bcrypt, jwt

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    # Registration logic here
    pass

@auth_bp.route('/login', methods=['POST'])
def login():
    # Login logic here
    pass

@auth_bp.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')
