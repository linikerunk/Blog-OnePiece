from django.contrib import admin
from .models import Categoria

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_link = ('id', 'nome_cat')# aqui para nós conseguirmos clicarmos na categoria..


admin.site.register(Categoria, CategoriaAdmin)