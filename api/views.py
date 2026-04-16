from django.shortcuts import render
from .models import Livre, Auteur

def dashboard(request):
    livres_count = Livre.objects.count()
    auteurs_count = Auteur.objects.count()
    livres_disponibles = Livre.objects.count()  # ✅ bien aligné

    return render(request, "dashboard.html", {
        "livres_count": livres_count,
        "auteurs_count": auteurs_count,
        "livres_disponibles": livres_disponibles,
    })