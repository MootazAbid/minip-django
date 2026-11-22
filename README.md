

On peut ajouter, voir, modifier et supprimer des demandes. On peut aussi changer leur statut.

 Technologies utilisées
- Python
- Django
- SQLite (base de données)
- HTML et CSS

 Ce que le site peut faire

- Voir la page d'accueil avec le nombre de demandes
- Voir la liste des demandes
- Voir les détails d'une demande
- Ajouter une demande
- Modifier une demande
- Supprimer une demande (avec une page de confirmation)
- Changer le statut : En attente, En cours de traitement ou Résolue
- Gérer les catégories et les demandes dans l'administration Django

Comment installer le projet

1. Ouvrir un terminal dans le dossier du projet (le dossier où se trouve `manage.py`).

2. Créer l'environnement virtuel :

python -m venv venv

3. Activer l'environnement virtuel :

venv\Scripts\activate

4. Installer Django :

pip install -r requirements.txt

5. Créer la base de données :

python manage.py makemigrations
python manage.py migrate

6. Créer un compte administrateur :

python manage.py createsuperuser

python manage.py runserver

 le navigateur :
- Le site : http://127.0.0.1:8000/
- L'administration : http://127.0.0.1:8000/admin/


 Les pages du site

| Page | Adresse |
|------|---------|
| Accueil | `/` |
| Liste des demandes | `/demandes/` |
| Détails d'une demande | `/demandes/1/` |
| Ajouter une demande | `/demandes/ajouter/` |
| Modifier une demande | `/demandes/modifier/1/` |
| Supprimer une demande | `/demandes/supprimer/1/` |

- `models.py` : les tables de la base de données (Categorie et Demande)
- `admin.py` : la configuration de l'administration
- `forms.py` : le formulaire pour ajouter et modifier une demande
- `views.py` : les fonctions qui préparent les pages
- `urls.py` : les adresses des pages
- `templates/maintenance/` : les pages HTML
- `static/maintenance/style.css` : le design du site

**Categorie** : nom, description 
**Demande** : titre, description, nom du demandeur, email, emplacement, catégorie, date de création, statut
Une catégorie peut avoir plusieurs demandes, mais une demande a une seule catégorie (relation ForeignKey).

