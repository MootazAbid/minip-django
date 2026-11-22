from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)  

    def __str__(self):
        return self.nom


class Demande(models.Model):
    STATUT_CHOICES = [
        ('attente', 'En attente'),
        ('en_cours', 'En cours de traitement'),
        ('resolue', 'Résolue'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    nom_demandeur = models.CharField(max_length=100)
    email = models.EmailField()
    emplacement = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name='demandes')
    date_creation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='attente')

    class Meta:
        ordering = ['-date_creation'] 

    def __str__(self):
        return self.titre

    def statut_suivant(self):
        if self.statut == 'attente':
            return 'en_cours'
        elif self.statut == 'en_cours':
            return 'resolue'
        else:
            return None
