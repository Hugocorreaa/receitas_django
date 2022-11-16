from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')

admin.site.register(Pessoa, ListandoPessoas)
