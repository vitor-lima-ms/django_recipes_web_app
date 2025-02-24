from django.test import TestCase
from recipes_app.models import Category, Recipe
from django.contrib.auth.models import User

'''Extraindo o setUp para outra classe'''
class RecipeTestBase(TestCase):
    '''Metodos setUp -> Deve executado antes de cada um dos testes'''
    def setUp(self): 
        #Outra forma de fazer
        # category = Category(name='Test category')
        # category.full_clean()
        # category.save() #Precisamos do save para criar id/PK
        # self.make_recipe() #Nao precisamos criar receitas para cada um dos testes
        return super().setUp()

    #Cria categorias separadamente
    def make_category(self, name='Default category'):
        return Category.objects.create(name = name)
    
    #Cria autores separadamente
    def make_author(
            self,
            first_name = 'First name',
            last_name = 'Last name',
            username = 'username',
            password = 'password',
            email = 'email@email.com',
    ):
        return User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password,
            email = email,
        )
    
    #Cria receitas separadamente
    def make_recipe(
            self,
            recipe_title = 'Recipe title',
            description = 'Description',
            slug = 'Slug',
            preparation_time = 999,
            preparation_time_unit = 'Time unit',
            servings = 999,
            servings_unit = 'Servings unit',
            preparation_steps = 'Preparation',
            preparation_steps_is_html = True,
            is_published = True,
            category_data = None,
            author_data = None,
    ):
        if category_data is None:
            category_data = {}
        
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            recipe_title = recipe_title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
            category = self.make_category(**category_data),
            author = self.make_author(**author_data),
        )