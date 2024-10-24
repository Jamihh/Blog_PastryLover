from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields =['titre', 'resume', 'contenu', 'image']
        widgets = {
            'titre' : forms.TextInput(attrs = {'class': 'form-control'}),
            'resume' : forms.TextInput(attrs={'class': 'form-control'}),
            'contenu' : forms.TextInput(attrs={'class': 'form-control'}),

        }