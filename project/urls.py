"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #include inclui as urls do app no urls.py da pasta principal do projeto
from django.conf.urls.static import static #Configurar os arquivos estaticos nas urls
from django.conf import settings #Permite importat configuracoes direto do arquivo settings.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes_app.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Para visualizar arquivos estaticos

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Para visualizar arquivos de midia
