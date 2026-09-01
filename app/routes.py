from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Module

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Affiche la liste de tous les modules enregistrés en base
@main.route('/modules')
def liste_modules():
    modules = Module.query.all()  # récupère tous les modules de la base
    return render_template('modules_liste.html', modules=modules)

# Formulaire de création d'un nouveau module.
# GET : affiche le formulaire vide. POST : traite les données envoyées
# par le formulaire et les enregistre en base de données.
@main.route('/modules/nouveau', methods=['GET', 'POST'])
def nouveau_module():
    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']
        categorie = request.form['categorie']

        nouveau = Module(nom=nom, description=description, categorie=categorie)
        db.session.add(nouveau)
        db.session.commit()

        # Une fois enregistré, on redirige vers la liste des modules
        return redirect(url_for('main.liste_modules'))

    return render_template('module_form.html')

# Affiche la fiche détaillée d'un module précis, identifié par son id
@main.route('/modules/<int:module_id>')
def detail_module(module_id):
    module = Module.query.get_or_404(module_id)
    return render_template('module_detail.html', module=module)
