"""admin."""
from django.contrib import admin

# Register your models here.

from .models import Receitas, Despesas, Aplicacoes

admin.site.register(Receitas)
admin.site.register(Despesas)
admin.site.register(Aplicacoes)
