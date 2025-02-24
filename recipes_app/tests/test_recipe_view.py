from recipes_app.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse #Obtem urls
from django.urls import resolve #Resolve qual funcao esta sendo usada por uma url
from recipes_app import views
from unittest import skip #Pula a classe toda ou um metodo especifico

# @skip('Mensagem do pq estou pulado estes testes.')
class RecipeViewsTest(RecipeTestBase): #RecipeTestBase ja herda TestCase, logo, RecipeViewsTest, herdando RecipeTestBase, tambem herda TestCase
    # '''Metodo tearDown -> Deve ser executado apos cada teste'''
    # def tearDown(self):
    #     return super().tearDown()

    '''Verificando a funcao presente em views'''
    def test_recipe_home_view_func_is_corrected(self):
        home_view = resolve(reverse('recipes_app:home'))
        self.assertIs(home_view.func, views.home) #Se utilizarmos o debugger, veremos que o home_view tem uma func, a qual queremos conferir se e igual a funcao home em views
    
    # @skip('Mensagem do pq estou pulando este teste.')
    def test_recipe_recipe_view_func_is_corrected(self):
        recipe_view = resolve(reverse('recipes_app:recipe', kwargs={'recipe_id': 1})) #Temos que passar um kwarg pos a funcao recipe em views recebe o request mais o id da recipe
        self.assertIs(recipe_view.func, views.recipe)
    
    def test_category_recipe_view_func_is_corrected(self):
        category_view = resolve(reverse('recipes_app:category', kwargs={'category_id': 1}))
        self.assertIs(category_view.func, views.category) #Is checa se duas coisas apontam para o mesmo endereco na memoria
    
    '''Verificando o status retornado e template renderizado'''
    
    #Home
    def test_recipe_home_view_returns_status_code_200_ok(self):
        response_home = self.client.get(reverse('recipes_app:home')) #self.client simula um usuario fazendo uma request get
        #Response tem um campo de status_code -> Da pra ver pelo debugger
        self.assertEqual(response_home.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response_home = self.client.get(reverse('recipes_app:home')) 
        self.assertTemplateUsed(response_home, 'recipes_app/pages/home.html') #O template passado aqui tem que estar presente na lista de templates utilizados para renderizar a pagina
    
    #Recipe
    def test_recipe_recipe_view_returns_status_code_200_ok(self):
        
        recipe = self.make_recipe() #Vou criar uma receita e atribuir a uma variavel para pegar o id dela dinamicamente

        response_recipe = self.client.get(reverse('recipes_app:recipe', kwargs={'recipe_id': recipe.id}))
        self.assertEqual(response_recipe.status_code, 200)

    def test_recipe_recipe_view_loads_correct_template(self):

        recipe = self.make_recipe() #Vou criar uma receita e atribuir a uma variavel para pegar o id dela dinamicamente

        response_recipe = self.client.get(reverse('recipes_app:recipe', kwargs={'recipe_id': recipe.id})) 
        self.assertTemplateUsed(response_recipe, 'recipes_app/pages/recipe.html')
    
     #Category
    def test_recipe_category_view_returns_status_code_200_ok(self):
        
        recipe = self.make_recipe() #Vou criar uma receita e atribuir a uma variavel para pegar o id da category dela dinamicamente

        response_category = self.client.get(reverse('recipes_app:category', kwargs={'category_id': recipe.category.id}))
        self.assertEqual(response_category.status_code, 200)

    def test_recipe_category_view_loads_correct_template(self):

        recipe = self.make_recipe() #Vou criar uma receita e atribuir a uma variavel para pegar o id da category dela dinamicamente

        response_category = self.client.get(reverse('recipes_app:category', kwargs={'category_id': recipe.category.id})) 
        self.assertTemplateUsed(response_category, 'recipes_app/pages/category.html')
    
    '''Verificando se a pagina ira renderizar corretamente caso nao haja receitas cadastradas (home)'''
    def test_recipe_home_show_no_recipes_if_no_recipes(self):
        # Recipe.objects.get(id=1).delete() #Criamos uma receita apenas no setUp, logo, sabemos que seu id/pk e 1 -> Como nao precisamos de receita aqui, podemos deleta-la
        response_home = self.client.get(reverse('recipes_app:home'))
        self.assertIn(
            '<img src="/static/recipes_app/img/empty.png" width="500">',
            response_home.content.decode('utf-8')) #O content do site vem codificado, por isso usamos decode para transformar em uma string
            #Mesmo com receitas cadastradas o teste passa pois o Django cria uma base de dados nova em memoria para cada um dos testes -> Ele nao esta usando a base de dados que esta exibindo as receitas cadastradas no site
        # self.fail('Lembrete para fazer alguma coisa.') #Sempre vai falhar o teste

    '''Testando recipe e category (404)'''
    def test_recipe_category_view_returns_status_code_404_if_no_recipe(self):
        response_category = self.client.get(reverse('recipes_app:category', kwargs={'category_id': int()})) #Precisamos passar um category id para a url para funcionar. Passando int(), que e =0, a receita nao existira e o teste funcionara
        self.assertEqual(response_category.status_code, 404)
    
    def test_recipe_recipe_view_returns_status_code_404_if_no_recipe(self):
        response_recipe = self.client.get(reverse('recipes_app:recipe', kwargs={'recipe_id': int()})) #Precisamos passar um recipe id para a url para funcionar. Passando int(), que e =0, a receita nao existira e o teste funcionara
        self.assertEqual(response_recipe.status_code, 404)
    
    '''Testando context e content (home)'''
    def test_recipe_home_template_loads_recipes(self): #Vamos criar categoria, autor e receita diretamente no codigo -> O objetivo e executar o site, pegar a resposta e ver se o context foi corretamente enviado e se o content foi corretamente exibido -> Nao precisamos criar aqui, podemos criar no setUp
        #Outra forma de fazer
        # category = Category(name='Test category')
        # category.full_clean()
        # category.save() #Precisamos do save para criar id/PK
        # fake_category = Category.objects.create(name='Test category')
        # fake_author = User.objects.create_user(
        #     first_name = 'First name',
        #     last_name = 'Last name',
        #     username = 'username',
        #     password = 'password',
        #     email = 'email@email.com',
        # )
        # fake_recipe = Recipe.objects.create(
        #     recipe_title = 'Recipe title',
        #     description = 'Description',
        #     slug = 'Slug',
        #     preparation_time = 999,
        #     preparation_time_unit = 'Time unit',
        #     servings = 999,
        #     servings_unit = 'Servings unit',
        #     preparation_steps = 'Preparation',
        #     preparation_steps_is_html = False,
        #     is_published = True,
        #     category = fake_category,
        #     author = fake_author,
        # )
        #Todo esse codigo acima e chamado de fixture -> Trecho de codigo utilizado para dar suporte ao teste

        self.make_recipe(recipe_title='Testing home content') #So precisamos de criar receitas aqui, os outros metodos nao precisam

        response = self.client.get(reverse('recipes_app:home')) #No debugger, podemos ver que o response tem um context -> Ele tem muitas coisas mas estamos interessados somente naquilo que injetamos no contexto a partir das funcoes em views -> No debug console digitar response.context['o que injetamos no context']
        '''
        self.assertEqual(len(response.context['recipes']), 1) #Criamos apenas uma receita acima e agora estamos checando se o response realmente retorna essa unica receita
        self.assertEqual(response.context['recipes'].first().recipe_title, 'Recipe title') #O context e uma QuerySet -> Como criamos apenas uma receita, podemos pegar o first de recipes e ver se o recipe_title e igual ao recipe_title que atribuimos a receita
        '''
        #Podemos testar diretamente no content, o que nos ajuda a determinar se o conteudo realmente apareceu na tela -> Podemos testar aqui, mas o mais usual e utilizar testes funcionais diretamente no navegador
        self.assertIn('Testing home content', response.content.decode('utf-8'))
        
        # self.assertIn('999' and 'Time unit', response.content.decode('utf-8')) #Podemos utilizar operadores logicos
    
    '''Testando context e content (recipe)'''
    def test_recipe_recipe_template_loads_recipe(self):

        recipe = self.make_recipe(recipe_title='Testing recipe content') #Criando uma receita, logo, id=1

        response = self.client.get(reverse('recipes_app:recipe', kwargs={'recipe_id': recipe.id})) #A view de recipe tem context recipe e title -> recipe recebe a receita -> title recebe o titulo da receita (recipe.recipe_title)
        #Tenho que passar recipe_id=1 aqui pq o make_recipe vai criar uma receita com id 1
        '''
        self.assertEqual(response.context['recipe'].id, 1) #O context recipe recebe a receita com id=1. Nao posso usar len pq sempre sera uma receita nesse template

        self.assertEqual(response.context['title'], 'Recipe title') #O context title recebe recipe_title='Recipe title'
        '''
        self.assertIn('Testing recipe content', response.content.decode('utf-8'))
        
        # self.assertIn('999' and 'Time unit', response.content.decode('utf-8'))
    
    '''Testando context e content (category)'''
    def test_recipe_category_template_loads_recipes(self):

        recipe = self.make_recipe(recipe_title='Testing category content', category_data={'name': 'Default category'}) #Criando uma receita, logo, id=1
        #Preciso passar um category_data senao category={} 

        response = self.client.get(reverse('recipes_app:category', kwargs={'category_id': recipe.id})) #A view de category tem context recipe e title -> recipe recebe as receitas da categoria -> title recebe uma fstring
        #Tenho que passar category_id=1 aqui pq o make_recipe vai criar uma category com id=1
        '''       
        self.assertEqual(len(response.context['recipes']), 1) #Aqui posso usar len pq uma category pode ter mais de uma receita

        self.assertEqual(response.context['title'], 'Default category - Categoria|') #O context title recebe recipe_title='Recipe title'
        '''
        self.assertIn('Testing category content', response.content.decode('utf-8'))
        
        # self.assertIn('999' and 'Time unit', response.content.decode('utf-8'))

    '''Verificando se as paginas nao exibem receitas nao publicadas'''
    #Home
    def test_recipe_home_template_dont_load_not_publi_recipes(self):

        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes_app:home'))

        self.assertIn(
            '<img src="/static/recipes_app/img/empty.png" width="500">',
            response.content.decode('utf-8'))
    
    #Recipe
    def test_recipe_recipe_template_dont_load_not_publi_recipes(self):

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes_app:recipe', kwargs={'recipe_id': recipe.id})) #id tem que ser 1 pois make_recipe so cria uma receita

        self.assertEqual(response.status_code, 404)
    
    #Category
    def test_recipe_category_template_dont_load_not_publi_recipes(self):

        recipe = self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes_app:category', kwargs={'category_id': recipe.id})) #id tem que ser 1 pois make_recipe so cria uma receita

        self.assertEqual(response.status_code, 404)