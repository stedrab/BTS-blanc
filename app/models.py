# app/models.py
# Chaque classe ici correspond à une table SQL, chaque attribut à une colonne.
# C'est le principe de l'ORM : on manipule des objets Python, SQLAlchemy
# traduit ça en requêtes SQL derrière.

from app import db

class Module(db.Model):
    __tablename__ = 'modules'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    categorie = db.Column(db.String(50))
    date_maj = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<Module {self.nom}>"
