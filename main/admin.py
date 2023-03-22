from django.contrib import admin

from main.models import Creations

class CreationsAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('titre', 'cree_a') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Creations, CreationsAdmin)
# Register your models here.
