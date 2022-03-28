from django.shortcuts import render

# Create your views here.
def pagina_bienvenida( request ):
    return render(request, 'bienvenida.html')

def pagina_principal( request ):
    return render(request, 'index.html')

