from ext import db
from sqlalchemy import Column , Integer , String , DateTime , Boolean , event
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
from datetime import datetime
from slugify import slugify
from farsisaz import slug_fa

class User(db.Model , UserMixin ):
    id = Column(Integer , primary_key=True)
    email = Column(String)
    password = Column(String)

    def __init__(self , email , password ):
        self.email = email
        self.password = generate_password_hash(password)

class Post(db.Model):
    id = Column(Integer , primary_key=True)
    titel = Column(String)
    text = Column(String)
    singer = Column(String)
    slug = Column(String)
    new = Column(String , default='')
    pic = Column(String)
    music = Column(String)
    time = Column(String , default = datetime.now())

    
    def save_slug(self):
        self.slug = slug_fa(self.titel)

    def update_slug(self):
        self.slug = slug_fa(self.titel)

