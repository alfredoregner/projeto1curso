# recipes/urls.py

from django.urls import path    # serve para importar a função do path do módulo de urls do django
from . import views             # Ter acesso a todas as funções e classes no arquivo views.py na pasta

urlpatterns = [                 # Onde coloca todas as definições dos caminhos
    #path('', views.home, name='recipes_home'), # View para dar home
    path('', views.recipe_list, name='recipe_list'), # Nova view para listar
]