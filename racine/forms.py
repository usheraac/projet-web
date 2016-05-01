#definition des models de nos formulaire
from django import forms
from .models import Publication

class nouvelle_PublicationForm(forms.Form):  #définition d'un formulaire pour les publications des utilisateur
    nom_lieu =forms.CharField(label="Nom du lieu touristique")
    description = forms.CharField(label="Description",widget=forms.Textarea)
    photo_1 =forms.ImageField(label="Ajouter une image de votre voyage")


class RechercheForm(forms.Form): #formulaire de recherche
    nom_recherche = forms.CharField(max_length=100, label ="Recherche")
