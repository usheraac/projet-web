from django.contrib import admin
from .models import Continent,Pays,Photo,SiteTouristique,Utilisateur,Video,Publication
# Register your models here.
admin.site.register(Continent) #referencement du models continent pour l'administration
admin.site.register(Pays)      #referencement du models pays pour l'administration
admin.site.register(Photo)     #referencement du models photo pour l'administration
admin.site.register(SiteTouristique)    #referencement du models Sitetouristique pour l'administration
admin.site.register(Utilisateur)        #referencement du models utilisateur pour l'administration
admin.site.register(Video)              #referencement du models video pour l'administration
admin.site.register(Publication)    #referencement du models publication
