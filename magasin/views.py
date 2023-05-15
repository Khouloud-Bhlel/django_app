from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Commande, Fournisseur
from .forms import ProduitForm, CommandeForm, FournisseurForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Produit

# Vues pour les produits
@login_required
def majProduits(request):
    produits = Produit.objects.all()
    return render(request, 'magasin/majProduits.html', {'produits': produits})

@login_required
def ajouterproduit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('majProduits')
    else:
        form = ProduitForm()
    return render(request, 'magasin/ajouterproduit.html', {'form': form})

@login_required
def modifierproduit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('majProduits')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'magasin/modifierproduit.html', {'form': form})

@login_required
def supprimerproduit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    produit.delete()
    return redirect('majProduits')

@login_required
def product_detail(request, produit_id):
    produit = get_object_or_404(Produit, id=produit_id)
    return render(request, 'magasin/produit_detail.html', {'produit': produit})

from django.shortcuts import redirect

def ajouter_au_panier(request, produit_id):
    produit = Produit.objects.get(pk=produit_id)
    panier = request.session.get('panier', {})
    panier[produit_id] = panier.get(produit_id, 0) + 1
    request.session['panier'] = panier
    return redirect('listecommandes')

#vitrine-----------------------------------------------------------------
@login_required
def vitrine(request):
   products= Produit.objects.all()
   context={'products':products}
   return render(request,'magasin/vitrinee.html',context)
#accueil-------------------------------------------------------------------
@login_required
def accueil(request): 
    return render(request, 'magasin/acceuil.html')
#commende------------------------------------------------------------------
@login_required
def listecommandes(request):
    commandes = Commande.objects.all()
    return render(request, 'magasin/listecommandes.html', {'commandes': commandes})

@login_required
def modifier_commande(request, pk):
    commande = get_object_or_404(Commande, pk=pk)
    form = CommandeForm(request.POST or None, instance=commande)

    if form.is_valid():
        form.save()
        return redirect('listecommandes')

    context = {
        'form': form,
        'commande': commande,
    }

    return render(request, 'magasin/modifier_commande.html', context)
@login_required
def supprimer_commande(request, pk):
    commande = Commande.objects.get(pk=pk)
    commande.delete()
    return redirect('listecommandes')
@login_required
def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            commande = form.save(commit=False)
            total = 0
            for produit_id in request.POST.getlist('produits'):
                produit = Produit.objects.get(id=int(produit_id))
                total += produit.prix
                commande.totalCde = total
                commande.save()
                commande.produits.add(produit)
            return redirect('listecommandes')
    else:
        form = CommandeForm()
    context = {
        'form': form
    }
    return render(request, 'magasin/ajouter_commande.html', context)


#index-----------------------------------------------------------------------------
@login_required
def index(request):
   
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)
#fournisseur-------------------------------------------------------------------
@login_required
def listeFournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    context = {'fournisseurs': fournisseurs}
    return render(request, 'magasin/listeFournisseurs.html', context)
@login_required
def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listeFournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/ajouter_fournisseur.html', {'form': form})
@login_required
def modifier_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('listeFournisseurs')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'magasin/modifier_fournisseur.html', {'form': form})
@login_required
def supprimer_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    fournisseur.delete()
    return redirect('listeFournisseurs')

#home-----------------------------------------------------------------------------------------------
@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'home.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user= authenticate(username=username,password=password)
            
            login(request, user)
            messages.success(request, f"Compte créé pour {username}!")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def login(request): 
    return render(request, 'registration/Login.html')
def loginout(request): 
    return render(request, 'registration/Logout.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Profile

@login_required
def user_details(request):
    return render(request, 'magasin/user_details.html', {'user': request.user})

#1ere endPoint-------------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie
from magasin.serializers import CategorySerializer
class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
#2eme endPoint-------------------------------------
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Produit
from .serializers import ProduitSerializer

class ProduitAPIView(APIView):

    def get(self, request):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
#3eme endPoint-------------------------------------
from rest_framework import viewsets
class ProductViewset(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProduitSerializer

    def get_queryset(self):
        queryset = Produit.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

