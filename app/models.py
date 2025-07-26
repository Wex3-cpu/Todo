# app/models.py
from app import db
from datetime import datetime

class Todo(db.Model):
    __tablename__ = 'todo'  # Explicitly set the table name
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    complete = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Todo {self.title}>'