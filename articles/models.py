from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    titre= models.CharField(max_length=150)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.CharField(max_length=250)
    contenu = models.TextField(blank=True)
    dateDePublication = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/images/', blank=True, null=True)
    
    def __str__(self):
     return f"{self.titre}"
   
    
