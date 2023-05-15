from django.urls import path, include
from .views import CategoryAPIView
from .views import ProduitAPIView
from rest_framework import routers
from magasin.views import ProductViewset, CategoryAPIView


from . import views

router = routers.SimpleRouter()
router.register('produit', ProductViewset, basename='produit')
urlpatterns = [
    path('', views.index, name='index'), 
    path('majProduits/', views.majProduits, name='majProduits'),
    path('ajouterproduit/', views.ajouterproduit, name='ajouterproduit'),
    path('modifierproduit/<int:pk>/', views.modifierproduit, name='modifierproduit'),
    path('supprimerproduit/<int:pk>/', views.supprimerproduit, name='supprimerproduit'),
    
    path('magasin/mesProduits/', views.index, name='mesProduits'),
    
    path('produit/<int:produit_id>/',views.product_detail, name='product_detail'),
    path('detail_produit/<int:produit_id>/ajouter_au_panier/',views.ajouter_au_panier, name='ajouter_au_panier'),
    #vitrine--------------------------------------------------------
    path('vitrine/', views.vitrine, name='vitrine'),
    #fournisseur-----------------------------------------------------------
    path('listeFournisseurs/', views.listeFournisseurs, name='listeFournisseurs'),
    path('ajouter_fournisseur/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('modifier_fournisseur/<int:pk>/', views.modifier_fournisseur, name='modifier_fournisseur'),
    path('supprimer_fournisseur/<int:pk>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    #user-----------------------------------------------------------
    path('register/',views.register, name = 'register'), 
    path('login/',views.login, name = 'login'),
    path('loginout/',views.loginout, name = 'loginout'),
    #home------------------------------------------------
    path('home/', views.home,name='home'),
    #acceuil------------------------------------------------
    path('accueil', views.accueil,name='accueil'),
    #index------------------------------------------------
    path('index/', views.index, name='index'), 
    #commende----------------------------------------------------------------
    path('listecommandes/', views.listecommandes, name='listecommandes'),
    path('ajouter_commande/', views.ajouter_commande, name='ajouter_commande'),
    path('modifier_commande/<int:pk>/', views.modifier_commande, name='modifier_commande'),
    path('supprimer_commande/<int:pk>/', views.supprimer_commande, name='supprimer_commande'),
    path('user_details/', views.user_details, name='user_details'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view(), name='produit_api'),
    path('api/', include(router.urls))
]

