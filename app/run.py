# Point d'entrée du programme : c'est ce fichier qu'on lance avec
# "python run.py" pour démarrer le serveur.

from app import create_app

# On appelle la fonction "usine" pour construire l'application Flask.
app = create_app()

# Vérifie qu'on exécute bien ce fichier directement (pas importé
# depuis un autre fichier).
if __name__ == '__main__':
    # debug=True affiche les erreurs détaillées dans le navigateur
    # et recharge le serveur automatiquement à chaque modification
    # du code. À désactiver plus tard en conditions réelles.
    app.run(debug=True)
