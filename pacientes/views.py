from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, Http404, HttpResponse
import json
import pandas as pd
from django.utils.encoding import uri_to_iri
from django.urls import reverse


from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from .forms import formulario_nuevo_paciente_principal, formulario_nuevo_paciente_modal
from .models import Paciente
from estudios.models import Estudio_Hemograma, Estudio_Embarazada, Estudio_Hepatograma, Estudio_Orina, Estudio_Urocultivo, \
        Estudio_Proteinograma, Estudio_Quimica, Estudio_Cultivo, Estudio_Parasitologico, Estudio_General

# Create your views here.

def nuevo_paciente( request ):
    if request.method == 'POST':
        form = formulario_nuevo_paciente_principal(request.POST)

        if form.is_valid():
            form.save()
            data = {
                'valid':form.is_valid()
            }

            return JsonResponse(data)
    else:
        form = formulario_nuevo_paciente_principal

    return render( request, 'nuevo_paciente.html', {'form':form} )

def paciente_nuevo_modal( request ):
    if request.method == 'POST':
        formulario = formulario_nuevo_paciente_modal(request.POST)

        if formulario.is_valid():
            formulario.save()
            data = {
                'valid':formulario.is_valid()
            }

            return JsonResponse(data)
    else:
        formulario = formulario_nuevo_paciente_modal

    return render( request, 'formularios/formulario_nuevo_paciente.html', {'formulario':formulario} )

def not_fund( request ):
    return render( request, '404.html')

class ver_paciente( DetailView ):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'ver_paciente.html'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('pacientes:404'))



    def get_context_data( self, **kwargs ):
        context = super( ver_paciente, self ).get_context_data(**kwargs )

        try:
            dni=Paciente
        except dni.DoesNotExist:
            raise Http404("Book does not exist")

        todos_los_estudios = (
                Estudio_Hemograma.objects.filter( paciente_id = self.object.dni ),
                Estudio_Embarazada.objects.filter( paciente_id = self.object.dni ),
                Estudio_Hepatograma.objects.filter( paciente_id = self.object.dni ),
                Estudio_Orina.objects.filter( paciente_id = self.object.dni ),
                Estudio_Urocultivo.objects.filter( paciente_id = self.object.dni ),
                Estudio_Proteinograma.objects.filter( paciente_id = self.object.dni ),
                Estudio_Quimica.objects.filter( paciente_id = self.object.dni ),
                Estudio_Cultivo.objects.filter( paciente_id = self.object.dni ),
                Estudio_Parasitologico.objects.filter( paciente_id = self.object.dni ),
                Estudio_General.objects.filter( paciente_id = self.object.dni )
            )

        estudios_del_paciente = ()

        for estudios_realizados in todos_los_estudios:
            
            if estudios_realizados.exists():
                estudios_del_paciente += ( tuple(estudios_realizados) )

        def estudio_ver( valor ):
            
            categorias = []
            for estudio in estudios_del_paciente:

                if valor == 'objeto':
                    categorias.append( estudio )
                    
                if valor == 'categoria':
                    categorias.append( estudio.categoria )

                if valor == 'fecha':
                    categorias.append( estudio.fecha_estudio )
                
            return categorias
        
        def mostrar_estudios_recientes( ):
            indices = []


            for i in range(len(estudios_del_paciente)):
                indices.append( str(i) )

            estudios = {
                'obj': estudio_ver('objeto'),
                'categoria': estudio_ver('categoria'),
                'fecha': estudio_ver('fecha'),

            }

            data_frame = pd.DataFrame( data=estudios, index=indices )
            data_frame['fecha'] =pd.to_datetime(data_frame['fecha'])

            data_frame = data_frame.sort_values( by='fecha', ascending=False)

            estudios_ordenados_recientes = data_frame['obj'].tolist()

            
            return estudios_ordenados_recientes
            

        context['estudios_del_paciente'] = mostrar_estudios_recientes()
               

        return context

def pacientes( request ):
    return render( request, 'pacientes.html')
'''
class editar_paciente( UpdateView ):
    model = Paciente
    form_class = formulario_nuevo_paciente_principal
    template_name = 'editar_paciente.html'
    success_url = '/'
'''
def editar_paciente( request, pk ):
    paciente = get_object_or_404(Paciente, pk = pk )


    if request.method == 'POST':
        form = formulario_nuevo_paciente_principal( request.POST or None, instance=paciente )
        if form.is_valid():
            form.save()
            data = {
                'valid':form.is_valid()
            }

            return JsonResponse(data)

    else:
        form = formulario_nuevo_paciente_principal( instance = paciente )
    
    contexto = {'form':form, 'dni':pk}

    return render( request, 'editar_paciente.html', contexto )
    
'''
class eliminar_paciente( DeleteView ):
    model = Paciente
    context_object_name = 'paciente'
    template_name = 'eliminar_paciente.html'
    success_url = '/'
'''

def eliminar_paciente( request, pk ):
    

    contexto = {'dni':pk}

    #return JsonResponse(data)
    return render( request, 'eliminar_paciente.html', contexto)

def confirmar_eliminacion_paciente( request ):
    post_data = json.loads( request.body.decode("utf-8") )
    dni_a_eliminar = post_data['elemento']
    
    
    
    paciente = get_object_or_404( Paciente, dni = dni_a_eliminar )

    paciente.delete()
    
    data = {
        'valid':True
    }

    return JsonResponse(data)

def ver_todos_filtro( request ):
    return render( request, 'menu_todos_los_pacientes.html')

class ver_todos_los_pacientes( ListView ):
    model = Paciente
    context_object_name = 'pacientes'
    template_name = 'todos_los_pacientes.html'
    paginate_by = 20

    def get_ordering( self ):
        ordenar_por = self.request.GET.get('ordering')
        ordering = self.request.GET.get('ordering', '-fecha_registro')

        if ordenar_por == 'fecha-registro':
            ordering = self.request.GET.get('ordering', '-fecha_registro')
        if ordenar_por == 'nombre':
            ordering = self.request.GET.get('ordering', 'nombre')
        if ordenar_por == 'apellido':
            ordering = self.request.GET.get('ordering', '-apellido')
        

        return ordering

    def get_context_data( self, *args, **kwargs):
        context = super( ver_todos_los_pacientes, self ).get_context_data( *args, **kwargs )

        #Solucion para mantener el filtrado durante todo el proceso de paginación
        # https://stackoverflow.com/questions/59972694/django-pagination-maintaining-filter-and-order-by
        
    
        context['order'] = self.get_ordering()
        return context

def ajax_get_view(request):
    post_data = json.loads( request.body.decode("utf-8") )
    dni_paciente = post_data['elemento']
    
    chequear_exitencia =  Paciente.objects.filter( dni = dni_paciente ).exists()

    if chequear_exitencia:
        paciente = Paciente.objects.get( dni = dni_paciente )
        nombre_completo_paciente = paciente.nombre + ' ' + paciente.apellido

        data = {
            'dni':chequear_exitencia,
            'paciente_nombre':nombre_completo_paciente
            
        }
    else:
        data = {
            'dni':chequear_exitencia,
            
        }


    return JsonResponse(data)
    
def obtener_dni( dni ):
    return dni

    