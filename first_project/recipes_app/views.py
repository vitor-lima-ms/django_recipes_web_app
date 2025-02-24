from django.shortcuts import render, get_list_or_404, get_object_or_404 #As duas funcoes get procuram uma lista de objetos ou um objeto unico os retornam caso existam. Caso nao, retorna o erro 404
from recipes_app.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes_app/pages/home.html', context={'recipes': recipes}) #Podemos passar variáveis, funcoes etc. no context

def recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, is_published=True) #O que vem apos o model sao filtros
    # recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipes_app/pages/recipe.html', context={'recipe': recipe, 'title': recipe.recipe_title})

def category(request, category_id):
    # recipes = Recipe.objects.filter(category__id=category_id).filter(is_published=True) #O dunder e para acessar o id do model Category a partir do atributo category do model Recipe (o atributo category do Recipe e uma FK de Category) -> [nome do campo no modelo]__[nome do campo do modelo de onde vem a FK]
    # if not recipes: #Se nao existirem receitas com o id informado
    #     raise Http404() #Levantamos o erro 404

    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')) #Usamos esse metodo para nao ter que fazer o if ali de cima

    # recipes = get_list_or_404(Recipe, category__id=category_id, is_published=True) #Pode ser feito assim tambem, mas nao conseguiriamos ordenar

    return render(request, 'recipes_app/pages/category.html', context={'recipes': recipes, 'title': f'{recipes[0].category} - Categoria|'}) #Como o get_list retorna uma lista, podemos usar a notacao de indice [indice] e nao o first() usado para QuerySet