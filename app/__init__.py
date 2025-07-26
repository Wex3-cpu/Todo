from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    
    # Ensure tables are created
    with app.app_context():
        try:
            from app.models import Todo  # Import your models here
            db.create_all()
            print("Tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")

    from app.routes import bp
    app.register_blueprint(bp)

    return app