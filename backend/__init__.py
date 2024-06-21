from flask import Flask
from flask_mongoengine import MongoEngine
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = MongoEngine()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from backend.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    return app
