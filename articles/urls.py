from turtle import home
from django.urls import path
from .views import home, modifier_article, new_article, supprimer_article, useradmin
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    
   
    path("", home, name='home'),  
    path("useradmin/", useradmin, name="useradmin"), 
    #path("accueil/", accueil, name="accueil"),
    #path('login/', login, name="login"),  # Page de connexion
    path("useradmin/new_article", new_article, name="new_article"),
    path("editarticle/<int:id>/", modifier_article, name="update"),
    path("supprimer_article/<int:id>/", supprimer_article, name="supprimer_article"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)