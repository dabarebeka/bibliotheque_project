from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.ForeignKey('Auteur', on_delete=models.CASCADE)
    date_ajout = models.DateField(auto_now_add=True)
    disponible = models.BooleanField(default=True)
    def __str__(self):
        return self.titre