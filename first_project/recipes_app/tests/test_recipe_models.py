from recipes_app.tests.test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError
from parameterized import parameterized
from recipes_app.models import Recipe #Como estou importando diretamente do models, e la que tenho que modificar os valores padrao para fazer os testes aq

#Parametros de modelos que alteram o comportamento da aplicacao, tem um valor max/min etc. devem ser testados e validados

class RecipeModelsTest(RecipeTestBase):
    def setUp(self): 
        self.recipe = RecipeTestBase.make_recipe(self)
        return super().setUp()
    
    def make_recipe_no_defaults(self):
        recipe = Recipe(
            recipe_title = 'Recipe title',
            description = 'Description',
            slug = 'Slug',
            preparation_time = 999,
            preparation_time_unit = 'Time unit',
            servings = 999,
            servings_unit = 'Servings unit',
            preparation_steps = 'Preparation',
            category = self.make_category( name='No default test - category'),
            author = self.make_author(username='No default test - username'),
        )
        
        recipe.full_clean() #Aqui ocorrem validacoes
        recipe.save() #Queremos testar a recipe salva na base de dados
        return recipe
    
    #So usamos o setUp aqui pq a maioria dos testes provavelmente vai precisar de uma receita
    
    @parameterized.expand( #De todas as formas descritas abaixo, essa e a melhor para parametrizar unittests -> Simula mto bem o pytest -> Ela cria um numero de testes igual a quantidade de tuplas passadas dentro da lista -> Funciona com o pytest 
            [
            ('recipe_title', 20),
            ('description', 200),
            ('preparation_time_unit', 20),
            ('servings_unit', 20),
        ] #Campos com max length
    )
    def test_recipe_fields_max_length(self, field, max_length):
        recipe = self.recipe
        
        '''for field, max_length in fields:
                with self.subTest(field=field, max_length=max_length): #Passamos como parametro os campos que mudam'''
        setattr(recipe, field, 'A' * (max_length + 1)) #Funcao que seta um valor ('A' * (max_length + 1)), para um campo (field) de um objeto (recipe) -> Para todos os campos, estamos setando um valor maior que o max_length, logo, o ValidationError sera levantado e o teste funcionara

        with self.assertRaises(ValidationError):
            recipe.full_clean()
            
        #O teste como esta escrito aponta apenas 1 falha, apesar dos 4 campos falharem. Dessa forma, nao e nem possivel saber qual campo falhou ou nao -> Podemos resolver isso utilizando uma ferramenta do unittest -> self.subtest -> So funciona com o python manage.py test

    def test_recipe_preparation_steps_is_html_is_false_by_default(self): #Apesar de ter um valor padrão, devemos testar uma vez que a variacao desse valor impacta diretamente no funcionamento do app
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.preparation_steps_is_html)
    
    def test_recipe_preparation_steps_is_published_is_false_by_default(self): #Apesar de ter um valor padrão, devemos testar uma vez que a variacao desse valor impacta diretamente no funcionamento do app
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(recipe.is_published)