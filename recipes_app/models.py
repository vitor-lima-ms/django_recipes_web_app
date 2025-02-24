from django.db import models
from django.contrib.auth.models import User #O User tambem sera uma tabela na nossa base de dados

# Create your models here.

class Category(models.Model): #Categorias possiveis para as receitas
    name = models.CharField(max_length=100)

    def __str__(self): #Funcao para mostrar o nome da categoria no painel de admin ao inves do id
        return self.name

class Recipe(models.Model): #As colunas da base dados serao os atributos da classe
    recipe_title = models.CharField(max_length=20) #CharField e um dos inumeros campos possiveis
    description = models.CharField(max_length=200)
    slug = models.SlugField() #Campo especial -> Ele e indexado -> Podemos utiliza-lo para buscar determinada receita -> Sem caracteres especiais
    #Podemos gerar um slug a partir do titulo com slugfy
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=20)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=20)
    preparation_steps = models.TextField() #Tipo um textarea do HTML
    preparation_steps_is_html = models.BooleanField(default=False) #O arquivo que contem os passos de preparacao e HTML?
    created_at = models.DateField(auto_now=True) #No momento da criacao, ele cria uma data e nao mexe mais nela
    updated_at = models.DateField(auto_now=True) #Data e atualizada a cada modificacao
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes_app/covers/%Y/%m/%d/', blank=True, default='') #Obtem dinamicamente ano, mes e dia -> Podemos tornar optional com o par blank=True e default
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None) #A coluna de categoria de uma Recipe recebe uma chave da tabela Category -> on_delete=models.SET_NULL indica que se uma categoria for apagada, a categoria da receita fica como null -> null=True permite que o campo seja nulo
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default='Anônimo')

    def __str__(self):
        return self.recipe_title