from django.contrib import admin
from recipes_app.models import Category, Recipe

# Register your models here.

class CategoryAdmin(admin.ModelAdmin): #Ao longo das aulas vamos adicionar configuracoes dentro da class
    ...
admin.site.register(Category, CategoryAdmin) #Passamos a classe e a classe adm associada a ela

@admin.register(Recipe) #Outra forma de registrar
class RecipeAdmin(admin.ModelAdmin):
    ...