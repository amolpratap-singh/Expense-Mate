
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    from app.models import User
    from app.routes import bp
    from app.forms import LoginForm
    
    with app.app_context():
        db.create_all()
    
    app.register_blueprint(bp)
    return app

