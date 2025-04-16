from app import db
from flask_login import UserMixin
from datetime import datetime
import pytz

india = pytz.timezone('Asia/Kolkata')
now = datetime.now(india)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150))
    email = db.Column(db.String(150), nullable = False,unique = True)
    password = db.Column(db.String(200), nullable= False)
    
    #one to many , one user manuy notes
    notes = db.relationship('Note', backref = 'author' , lazy= True)
    
    
    def __repr__(self):
        return f"<User {self.username}>"
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default = now)
    date_updated = db.Column(db.DateTime, onupdate= now)

    #forien key to User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __repr__(self):
        return f"<Note {self.id}>"

from app import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))