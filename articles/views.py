from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
import articles
from articles.forms import ArticleForm
from articles.models import Article


# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles":articles} )


def useradmin(request):
    articles = Article.objects.all() # Récupère tous les articles
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False) # Ne pas enregistrer encore
            article.auteur = request.user # Assignation de l'auteur
            article.save() # Enregistre l'article
            messages.success(request, 'Article ajouté avec succes !')
            return redirect('useradmin') # Redirige après succès
    else:
      form = ArticleForm() # Formulaire vide si la requête est GET
      
    return render(request, 'useradmin.html', {'form': form , 'articles': articles })
    
    #return render(request, 'useradmin.html', {'form': form})

def new_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.save()
            messages.success(request, 'Article ajouté avec succès !')
            return redirect('useradmin')
    else:
        form = ArticleForm()

    return render(request, 'new_article.html', {'form': form })

def useradmin(request):
    articles = Article.objects.all()  # Récupérer tous les articles
    return render(request, 'useradmin.html', {'articles': articles})


def modifier_article(request, id):
    #récupération de l'article à partir de son ID
    article = get_object_or_404(Article, id=id)
    
    if request.method == 'POST':
        edit_form = ArticleForm(request.POST, request.FILES, instance = article)
        
        if edit_form.is_valid():
            edit_form.save()
            return redirect('useradmin')
    else:
        edit_form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'edit_form': edit_form, 'article': article})

def supprimer_article(request, id):
    article = get_object_or_404(Article, pk=id)
    article.delete()
    messages.success(request, 'Article supprimé avec succès !')
    return redirect('useradmin')



# def new_article(request):
#     auteur= request.user
#     titre= request.POST['titre']
#     contenu= request.POST['contenu']
#     resume= request.POST['resume']
#     article=Article.objects.create(
#         auteur=auteur,
#         titre=titre,
#         resume=resume,
#         contenu=contenu
#     )
#     article.save()
#     messages.success(request, 'Article ajouté avec succés !')
#     return redirect('ajouter_article')
# 
#     return render(request, "new_article.html")
