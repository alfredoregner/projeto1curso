from django.shortcuts import render, get_object_or_404

from .models import Recipe

#from django.http import HttpResponse

# Create your views here.

#def home(request):
#    return HttpResponse("<h1>Bem-vindo à página de Receitas!<h1> \nE não é que funciona mesmo essa budega aqui...")

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes':recipes})

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'recipe':recipe})