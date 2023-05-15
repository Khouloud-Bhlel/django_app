from rest_framework.serializers import ModelSerializer
from magasin.models import Categorie
class CategorySerializer(ModelSerializer):
 
    class Meta:
        model = Categorie
        fields = ['id', 'name']

from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    categorie_id = serializers.IntegerField(source='categorie.id')

    class Meta:
        model = Produit
        fields = ['id', 'libelle', 'description', 'categorie_id']
