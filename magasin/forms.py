from django.forms import ModelForm 
from .models import Produit 
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Commande
from django.forms import ModelForm
from .models import Fournisseur
#produit---------------------------
class ProduitForm(ModelForm): 
    class Meta : 
        model = Produit 
        fields = "__all__" 
        
#commende------------------------------
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = "__all__" 
#Fournisseur-------------------------- 
class FournisseurForm(ModelForm):
    class Meta:
        model = Fournisseur
        fields = '__all__'
#registre------------------------------
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control-file'}))

