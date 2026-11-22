from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Demande, Categorie
from .forms import DemandeForm


def accueil(request):
    total = Demande.objects.count()
    nb_attente = Demande.objects.filter(statut='attente').count()
    nb_en_cours = Demande.objects.filter(statut='en_cours').count()
    nb_resolues = Demande.objects.filter(statut='resolue').count()
    dernieres = Demande.objects.all()[:5]

    contexte = {
        'total': total,
        'nb_attente': nb_attente,
        'nb_en_cours': nb_en_cours,
        'nb_resolues': nb_resolues,
        'dernieres': dernieres,
    }
    return render(request, 'maintenance/home.html', contexte)


def liste_demandes(request):
    demandes = Demande.objects.all()
    categories = Categorie.objects.all()

    # Filtres facultatifs (dans l'URL : ?categorie=1&statut=attente)
    categorie_id = request.GET.get('categorie')
    statut = request.GET.get('statut')
    if categorie_id:
        demandes = demandes.filter(categorie_id=categorie_id)
    if statut:
        demandes = demandes.filter(statut=statut)

    contexte = {
        'demandes': demandes,
        'categories': categories,
        'statuts': Demande.STATUT_CHOICES,
        'categorie_choisie': categorie_id,
        'statut_choisi': statut,
    }
    return render(request, 'maintenance/demande_list.html', contexte)


def detail_demande(request, pk):
    demande = get_object_or_404(Demande, pk=pk)
    contexte = {
        'demande': demande,
        'statuts': Demande.STATUT_CHOICES,
    }
    return render(request, 'maintenance/demande_detail.html', contexte)


def ajouter_demande(request):
    if request.method == 'POST':
        form = DemandeForm(request.POST)
        if form.is_valid():
            demande = form.save()
            messages.success(request, "La demande a été ajoutée avec succès.")
            return redirect('detail_demande', pk=demande.pk)
    else:
        form = DemandeForm()
    return render(request, 'maintenance/demande_form.html',
                  {'form': form, 'titre_page': 'Ajouter une demande'})


def modifier_demande(request, pk):
    demande = get_object_or_404(Demande, pk=pk)
    if request.method == 'POST':
        form = DemandeForm(request.POST, instance=demande)
        if form.is_valid():
            form.save()
            messages.success(request, "La demande a été modifiée avec succès.")
            return redirect('detail_demande', pk=demande.pk)
    else:
        form = DemandeForm(instance=demande)
    return render(request, 'maintenance/demande_form.html',
                  {'form': form, 'titre_page': 'Modifier la demande', 'demande': demande})


def supprimer_demande(request, pk):
    demande = get_object_or_404(Demande, pk=pk)
    if request.method == 'POST':
        demande.delete()
        messages.success(request, "La demande a été supprimée.")
        return redirect('liste_demandes')
    return render(request, 'maintenance/demande_confirm_delete.html', {'demande': demande})


def changer_statut(request, pk):
    demande = get_object_or_404(Demande, pk=pk)
    if request.method == 'POST':
        nouveau_statut = request.POST.get('statut')
        statuts_valides = [code for code, nom in Demande.STATUT_CHOICES]
        if nouveau_statut in statuts_valides:
            demande.statut = nouveau_statut
            demande.save()
            messages.success(request, "Le statut est maintenant : " + demande.get_statut_display() + ".")
        else:
            messages.error(request, "Statut invalide.")
    retour = request.POST.get('retour')
    if retour == 'liste':
        return redirect('liste_demandes')
    return redirect('detail_demande', pk=demande.pk)
