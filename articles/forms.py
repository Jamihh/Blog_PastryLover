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
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d utilisateur'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))