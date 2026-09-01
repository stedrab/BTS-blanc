from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# On crée l'objet "db" ici, hors de create_app, pour pouvoir l'importer
# facilement depuis d'autres fichiers (comme models.py).
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # On lie l'objet db à l'application Flask.
    db.init_app(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
