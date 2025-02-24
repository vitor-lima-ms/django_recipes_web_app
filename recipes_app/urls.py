from django.urls import path
from recipes_app import views

app_name = 'recipes_app'

urlpatterns = [
    path('', views.home, name='home'), #name e utilizado para dar um nome unico
    path('recipe/<int:recipe_id>/', views.recipe, name='recipe'), #<id> vai automaticamente como parametro para recipe. Nao precisa ser id, pode ser outra palavra. Path converter antes : sem espaco id ou outra identificacao
    path('recipe/category/<int:category_id>/', views.category, name='category')
]