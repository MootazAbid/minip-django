from django.contrib import admin
from .models import Categorie, Demande


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)


class DemandeAdmin(admin.ModelAdmin):
    list_display = ('titre', 'nom_demandeur', 'categorie', 'statut', 'date_creation')
    list_filter = ('statut', 'categorie')
    search_fields = ('titre', 'nom_demandeur', 'email')


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Demande, DemandeAdmin)
