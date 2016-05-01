"""mosac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#référencement des différents liens vers les pages web
urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$','racine.views.index', name ='index' ),
    url(r'^index','racine.views.index', name='index'),
    url(r'^publier','racine.views.publier', name='publier'),
    url(r'^europe','racine.views.europe', name ='europe'),
    url(r'^asie','racine.views.asie', name ='asie'),
    url(r'^amerique','racine.views.amerique', name ='amerique'),
    url(r'^oceanie','racine.views.oceanie', name ='oceanie'),
    url(r'^afrique','racine.views.afrique', name ='afrique'),
    url(r'^a-ne-pas-rater','racine.views.a_ne_pas_rater', name ='a-ne-pas-rater'),
    url(r'^au-bord-de-mer','racine.views.au_bord_de_mer', name ='au-bord-de-mer'),
    url(r'^vivre-la-montagne','racine.views.vivre_la_montagne', name='vivre-la-montagne'),
    url(r'^citytrips','racine.views.citytrips', name ='citytrips'),
    url(r'^aventure','racine.views.aventure', name ='aventure')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
