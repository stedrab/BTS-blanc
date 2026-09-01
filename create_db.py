# create_db.py
# À exécuter une fois pour créer les tables dans la base de données,
# à partir des modèles définis dans app/models.py.

from app import create_app, db
from app.models import Module

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables créées avec succès.")
