import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://wex:V4R9lPPj3HGF6u0YuLdwXLRwT0hxQq4C@dpg-d21pau3ipnbc73fp9clg-a.oregon-postgres.render.com/wexoniii'
    SQLALCHEMY_TRACK_MODIFICATIONS = False