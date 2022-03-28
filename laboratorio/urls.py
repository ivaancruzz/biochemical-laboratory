from django.urls import path, include

from .views import pagina_bienvenida, pagina_principal

app_name = 'laboratorio'

urlpatterns = [
    path('bienvenida/', pagina_bienvenida, name='pag_bienvenida' ), #Pagina de bienvenida
    
    path('', pagina_principal, name='pag_principal' ), #Pagina principal INDEX
]
