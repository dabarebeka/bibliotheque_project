from django.contrib import admin
from .models import Livre, Auteur

# PERSONNALISATION LIVRE
class LivreAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'disponible', 'date_ajout')
    list_filter = ('disponible', 'date_ajout')
    search_fields = ('titre',)

# PERSONNALISATION AUTEUR
class AuteurAdmin(admin.ModelAdmin):
    search_fields = ('nom',)

admin.site.register(Livre, LivreAdmin)
admin.site.register(Auteur, AuteurAdmin)
admin.site.site_header = "📚 Bibliothèque Admin"
admin.site.site_title = "Admin Django"
admin.site.index_title = "Bienvenue Rebeka 👋"