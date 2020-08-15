from nza_2 import app, db, login
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User Class
class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    note = db.relationship('Note', backref='author', lazy=True )

    def __init__(self,username,email,password):
        self.username= username
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with {self.email}'
# Notes Class
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    case = db.Column(db.String(200))
    case_note = db.Column(db.String(500))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    
    def __init__(self, case, case_note, user_id):
        self.case = case
        self.case_note = case_note
        self.user_id = user_id

    def __repr__(self):
        return f'The name of the case is {self.case} \n and the notes are {self.case_note}'