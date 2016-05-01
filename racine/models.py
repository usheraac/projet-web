from django.db import models
from django.forms import ModelForm
from django.core.files.storage import FileSystemStorage
# Create your models here.

fs = FileSystemStorage(location ='/media/') #declaration d'une variable de stockage

#objets de stockage à l'image de la base de données

 #définiton du models continent
class Continent(models.Model):
    nom_continent = models.CharField(max_length=100 )
    description_continent = models.CharField(max_length=1000,blank = True)
    lien_wiki_continent = models.CharField(max_length=255,blank = True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.nom_continent



#définiton du models pays
class Pays(models.Model):
    nom_pays = models.CharField(max_length=255)
    description_pays = models.CharField(max_length=1000,blank = True)
    lein_wiki_pays = models.CharField(max_length=255,blank = True)

    def __str__(self):
        return self.nom_pays


 #définiton du models photos
class Photo(models.Model):
    nom_photo = models.CharField(max_length=255)
    photo = models.ImageField(upload_to= "media/")

    def __str__(self):
        return self.nom_photo







#définiton du models SiteTouristique
class SiteTouristique(models.Model):
    nom_site = models.CharField(max_length=255)
    description_site = models.CharField(max_length=1000,blank = True)
    photo = models.ImageField(storage=fs)

    def __str__(self):
        return self.nom_site



 #définiton du models utilisateur
class Utilisateur(models.Model):
    nom_user = models.CharField(max_length=255)
    prenom_user = models.CharField(max_length=255,blank = True)
    email_user = models.CharField(max_length=255,blank = True)

    def __str__(self):
        return self.nom_user

#définiton du models video
class Video(models.Model):
    nom_videos = models.CharField(max_length=255)
#    date_videos = models.DateTimeField()

    def __str__(self):
        return self.nom_video



class Publication(models.Model):  #définition d'un model qui servira de  formulaire pour les publications des utilisateurs
    nom_lieu = models.CharField(max_length=100)
    description = models.TextField()
    photo_1 = models.ImageField(upload_to= "media/")

    def __str__(self):
        return self.nom_lieu
