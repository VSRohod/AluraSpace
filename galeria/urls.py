from django.urls import path
from galeria.views import index, imagem

# create lists to organizate the urls

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
]
