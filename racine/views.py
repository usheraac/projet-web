
from django.shortcuts import render
from .models import Continent,Pays,Photo,SiteTouristique,Utilisateur,Video,Publication
from .forms import nouvelle_PublicationForm, RechercheForm
from django.db.models import Q
import re

# Create your views here.
def index(request): #views pour la page index.html
    #definition de la fonction recherce pas encore actif
    if request.method =='POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            nom_recherche = form.cleaned_data['nom_recherche']
            envoi = True
    else:
        form = RechercheForm()#instanciation de la classe RechercheForm qui crée un formulaire
        publications =Publication.objects.order_by('-id')[:3]#requête dans la base de données pour recupérer les 3 dernières entrée par odre d'id
        a,b,c = publications #deballage des la liste d'objet "publications" dans les variables a,b et c

    return render(request,'index.html', {'a':a,'b':b,'c':c}) #redirection vers la page "index.html" avec transmition des objets a,b et c

def accueil(request):  #views pour la page acceuil.html

    return render(request,'accueil.html')

def europe(request):  #views pour la page europe.html
    return render(request,"europe.html")

def afrique(request):  #views pour la page afrique.html
    return render(request,"afrique.html")

def amerique(request):  #views pour la page amerique.html
    return render(request, "amerique.html")

def asie(request):  #views pour la page asie.html
    return render(request,"asie.html")

def oceanie(request):  #views pour la page oceanie.html
    return render(request, "oceanie.html")

def a_ne_pas_rater(request):    #views pour la page a-ne-pas-rater.html
    return render(request,"a-ne-pas-rater.html")

def au_bord_de_mer(request): #views pour la page au_bord_de_mer
    return render(request, "au-bord-de-mer.html")

def vivre_la_montagne(request):  #views pour la page vivre_la_montagne
    return render(request,"vivre-la-montagne.html")

def citytrips(request): #views pour la page citytrips
    return render(request,"citytrips.html")

def aventure(request): #views pour la page aventure
    return render(request,"aventure.html")

def publier(request):  #views pour la page publier.html
    envoi = False
    sauvegarde = True
    if request.method =='POST':
        form = nouvelle_PublicationForm(request.POST, request.FILES)#isntanciation de la classe publicationform pour generer des formulaire de publication
        #validation et filtrage des donnés fournies par le user  pour les lignes qui  suivent
        if form.is_valid(): #validation
            valeur = Publication()
            valeur.nom_lieu =  form.cleaned_data['nom_lieu'] #filtrage
            valeur.description = form.cleaned_data['description']
            valeur.photo_1 = form.cleaned_data["photo_1"]
            valeur.save()
            envoi = True
            sauvegarde = False
            publications =Publication.objects.order_by('-id')[:3] #idem que pour la fonction "index" plus haut
            a,b,c = publications
            return render(request,'index.html', {'a':a,'b':b,'c':c})
    else:
        form = nouvelle_PublicationForm()
    return render(request,'publier.html', locals())


#cette n'est pas encore activé
def recherche(request): #définition la fonction recherche et gestion des entreés
    if request.method =='POST':
        form = RechercheForm(request.POST)
        if form.is_valid():
            nom_recherche = form.cleaned_data['nom_recherche']
            envoi = True
    else:
        form = RechercheForm()
    return render(request, 'index.html', locals())
