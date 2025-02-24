from django.test import TestCase
from django.urls import reverse #Obtem urls

class RecipeURLsTest(TestCase):  #Todo metodo dessa classe que comecar com o padrao definido em pytest.ini sera um test
    # def test_the_pytest_is_ok(true): #pytest -rP executa o teste e o print que estiver dentro dele
    #     ...
    #Os testes vao nos ajudar a entender o Django

    def test_recipe_home_url_is_correct(self):
        # assert 1 != 1 #Usamos so para fazer o teste falhar
        # self.assert #Muitos tipos de assert
        home_url = reverse('recipes_app:home')
        self.assertEqual(home_url, '/') #Estamos testando se a url da home realmente é /
    
    def test_recipe_category_url_is_correct(self):
        category_url = reverse('recipes_app:category', kwargs={'category_id': 1}) #Podemos passar args tambem, ordem
        self.assertEqual(category_url, '/recipe/category/1/')
    
    def test_recipe_recipe_url_is_correct(self):
        recipe_url = reverse('recipes_app:recipe', kwargs={'recipe_id': 1}) #Podemos passar args tambem, ordem
        self.assertEqual(recipe_url, '/recipe/1/')