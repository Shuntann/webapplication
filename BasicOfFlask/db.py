from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app) 


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), nullable=False)#nullable=flaseにすることで必須項目にする
    detail = db.Column(db.String(100))
    due = db.Column(db.DateTime, nullable=False)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()