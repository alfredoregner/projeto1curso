from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField(help_text="Tempo em minutos")
    image = models.ImageField(upload_to='recipes/', blank=True, null=True) #upload_to='recipes/' significa que as imagens serão salvas em MEDIA_TOOR/recipes


    def __str__(self):
        return self.title
    
    class Meta:
        #Define o nome da tabela no plural para o painel de administração
        verbose_name_plural = "Recipes"