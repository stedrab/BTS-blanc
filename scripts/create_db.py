# create_db.py
# À exécuter une fois pour créer les tables dans la base de données,
# à partir des modèles définis dans app/models.py.
# Lancement depuis la racine du projet : python scripts/create_db.py

import os
import sys
# On ajoute la racine du projet au chemin pour pouvoir importer le package 'app'
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models import Module

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables créées avec succès.")
