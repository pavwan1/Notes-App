from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()
csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'main.login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = 'info'     # flash category



def create_app():   
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = 'mysecretkey'
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
    
    #extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    
    #blueprint for routes
    from app.routes import main
    app.register_blueprint(main)
    
    # 🔁 Later: Register blueprints here (e.g., auth, notes, etc.)
    
    return app

