# BTS-blanc — Documentation KNX

Application web **Flask** de gestion d'une documentation de modules KNX,
réalisée dans le cadre d'un projet de BTS.

## Fonctionnalités

- Page d'accueil
- Liste des modules enregistrés
- Création d'un nouveau module (formulaire)
- Fiche détaillée d'un module

## Arborescence

```
.
├── app/                     # Package principal de l'application
│   ├── __init__.py          # Usine Flask (create_app) + init de la base
│   ├── config.py            # Configuration (URI base de données)
│   ├── models.py            # Modèles SQLAlchemy (table "modules")
│   ├── routes.py            # Routes / vues (Blueprint "main")
│   ├── static/              # Fichiers statiques (CSS, images…)
│   └── templates/           # Templates Jinja2 (HTML)
├── scripts/                 # Scripts utilitaires
│   └── create_db.py         # Création des tables en base
├── docs/                    # Documentation du projet (cahier des charges, revues…)
├── requirements.txt         # Dépendances Python
└── run.py                   # Point d'entrée : lance le serveur
```

> Note : `run.py`, `requirements.txt`, `README.md` et `.gitignore` restent à
> la racine — c'est la convention Python/GitHub et l'application en a besoin
> pour démarrer.

## Installation

```bash
# 1. Créer et activer un environnement virtuel
python3 -m venv venv
source venv/bin/activate        # sous Windows : venv\Scripts\activate

# 2. Installer les dépendances
pip install -r requirements.txt
```

## Configuration de la base de données

La connexion à la base MySQL se règle dans `app/config.py`
(`SQLALCHEMY_DATABASE_URI`). Remplacer l'utilisateur, le mot de passe
et le nom de la base par les tiens.

> ⚠️ Ne jamais committer de vrai mot de passe. Pour un vrai secret,
> le placer dans un fichier `.env` (déjà ignoré par `.gitignore`).

Créer ensuite les tables (à lancer depuis la racine du projet) :

```bash
python scripts/create_db.py
```

## Lancement

```bash
python run.py
```

Le serveur démarre sur http://127.0.0.1:5000
