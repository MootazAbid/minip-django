from django import forms
from .models import Demande


class DemandeForm(forms.ModelForm):

    class Meta:
        model = Demande
        fields = ['titre', 'description', 'nom_demandeur', 'email',
                  'emplacement', 'categorie', 'statut']
        labels = {
            'titre': 'Titre',
            'description': 'Description du problème',
            'nom_demandeur': 'Nom du demandeur',
            'email': 'Adresse e-mail',
            'emplacement': 'Emplacement (salle, bureau...)',
            'categorie': 'Catégorie',
            'statut': 'Statut',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_titre(self):
        titre = self.cleaned_data['titre'].strip()
        if len(titre) < 5:
            raise forms.ValidationError("Le titre doit contenir au moins 5 caractères.")
        return titre

    def clean_description(self):
        description = self.cleaned_data['description'].strip()
        if len(description) < 10:
            raise forms.ValidationError("La description doit contenir au moins 10 caractères.")
        return description

    def clean_nom_demandeur(self):
        nom = self.cleaned_data['nom_demandeur'].strip()
        for lettre in nom:
            if lettre.isdigit():
                raise forms.ValidationError("Le nom ne doit pas contenir de chiffres.")
        return nom
