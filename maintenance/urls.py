from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('demandes/', views.liste_demandes, name='liste_demandes'),
    path('demandes/ajouter/', views.ajouter_demande, name='ajouter_demande'),
    path('demandes/<int:pk>/', views.detail_demande, name='detail_demande'),
    path('demandes/modifier/<int:pk>/', views.modifier_demande, name='modifier_demande'),
    path('demandes/supprimer/<int:pk>/', views.supprimer_demande, name='supprimer_demande'),
    path('demandes/statut/<int:pk>/', views.changer_statut, name='changer_statut'),
]
