from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.http import HttpResponse, JsonResponse

from pacientes.models import Paciente
from django.urls import reverse
import json


from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf



from .models import Estudio_Hemograma, Estudio_Embarazada, Estudio_Hepatograma, Estudio_Orina, Estudio_Urocultivo, \
        Estudio_Proteinograma, Estudio_Quimica, Estudio_Cultivo, Estudio_Parasitologico, Estudio_General


from .forms import formulario_estudio_hemograma, formulario_estduio_embarazada, formulario_estduio_hepatograma, formulario_estduio_orina,\
        formulario_estduio_urocultivo, formulario_estduio_proteinograma, formulario_estduio_quimica, \
        formulario_estduio_cultivo, formulario_estduio_parasitologico, formulario_estudio_general, formulario_nueva_caratula

# Create your views here.
def estudios_page( request ):
        return render(request, 'estudios.html')



def buscar_estudio_por_id_y_categoria( id_estudio, categoria ):
        categoria = int(categoria) #Convertimos la categoria a entero para poder comparar luego

        #Guardamos todos los estudios
        todos_los_estudios = [
                Estudio_Embarazada,
                Estudio_Hepatograma,
                Estudio_Orina,
                Estudio_Urocultivo, 
                Estudio_Proteinograma,
                Estudio_Quimica,
                Estudio_Cultivo,
                Estudio_Parasitologico,
                Estudio_Hemograma,
                Estudio_General,
        ]
        
        
        #categoria_estudio es 1..2..3..4..
        for categoria_estudio in range(len(todos_los_estudios)):
                #Si la categoria del parametro es igual al del recorrido
                if categoria is categoria_estudio:
                        #Buscamos si esta el estudio por su id y guardamos el objeto
                        estudio = todos_los_estudios[categoria_estudio].objects.filter( id = id_estudio )

        return estudio




def ver_estudio( request, id_estudio, categoria, paciente_id ):
        
        estudio = buscar_estudio_por_id_y_categoria( id_estudio, categoria )
        #Obtenemos el nombre, fecha del estudio  y nomb del paciente por separado para luego mostrarlo
        for ver in estudio:
                nombre_del_estudio = ver
                categoria_estudio = ver.categoria
                fecha_del_estudio = ver.fecha_estudio
                datos_paciente = Paciente.objects.get( dni = ver.paciente_id )
        

        if categoria_estudio == 9:
                resultados_js = convertir_estudio_general_para_imprimir( resultados_del_estudio(estudio) )
        else:
                resultados_js = pasar_resultados_a_string( resultados_del_estudio(estudio) )

        #Datos paciente alterados
        nombre_paciente = datos_paciente.nombre +' '+datos_paciente.apellido
        fecha_del_estudio = f'{fecha_del_estudio.day} / {fecha_del_estudio.month} / {fecha_del_estudio.year}'

        observaciones_js = convertir_observacion_para_imprimir( estudio )
        contexto = {
                #Datos paciente
                'nombre_paciente': nombre_paciente,
                'nombre_estudio':nombre_del_estudio,
                

                #Datos resultados
                'categoria_estudio':categoria_estudio,
                'fecha_estudio':fecha_del_estudio, 
                'resultados':resultados_del_estudio( estudio ),
                'observacion':observacion_estudio( estudio ),
                'resultadosJS': resultados_js,
                'observaciones_js': observaciones_js,
                }

        return render( request, 'ver_estudio.html',contexto )
def convertir_estudio_general_para_imprimir( estudio ):
        string = ''
        
        detalle = estudio[1][1]

        x = detalle.replace('\r\n', '´')

        print(x)

        estudio[1][1] = x

        print(estudio) 
                

        for i in estudio:
                string += i[0] + '_'
                string += i[1] + '_'
                string += '**'

      
        
        return string

def convertir_observacion_para_imprimir(estudio):
        observacion = None

        try:
                for ver in estudio:
                        observacion = ver.observaciones
                
                if( observacion is not None):
                        x = observacion.replace('\r\n', '´')
                else:
                        x = 'Ninguna'

                print(x)

                observacion = x
        
        except AttributeError:
                print('El estudio GENERAL no tiene la columna observaciones')

        
        return observacion
        

class editar_estudio( UpdateView ):
        model = Estudio_Embarazada
        form_class = formulario_estduio_embarazada
        template_name = 'formularios/estudio_embarazada.html'
        success_url = '/'

def editar_estudio( request, id_estudio, categoria ):
        obj_and_form = get_obj_form( id_estudio, categoria )
        form = obj_and_form['get_formulario'](request.POST or None, instance= obj_and_form['get_modelo'])
        

        if request.method == 'POST':
                
                if form.is_valid():
                        form.save()
                        data = {
                                'valid':form.is_valid()
                        }

                        return JsonResponse(data)
        else:
                context_csrf = {}
                context = {}

                dni_paciente = obj_and_form['get_modelo'].paciente_id

                context_csrf.update(csrf(request))

                context['id'] = id_estudio
                context['categoria'] = categoria

                form_html = render_crispy_form( form, helper = None, context = context_csrf )
                context['form'] = form_html

        return render( request, 'editar_estudio.html', context )

def eliminar_estudio( request, id_estudio, categoria ):

        estudio = buscar_estudio_por_id_y_categoria(id_estudio,categoria)

        for ver in estudio:
                dni_paciente = ver.paciente_id
       
        
        contexto = {
                'id': id_estudio,
                'categoria': categoria,
                'dni':dni_paciente,
                
        }
        return render( request, 'eliminar_estudio.html', contexto )

def confirm_eliminacion_estudio( request ):
        post_data = json.loads( request.body.decode("utf-8") )
        id_estudio = post_data['elemento']
        categoria_estudio = post_data['elemento2']
        
        modelo = get_obj_form( id_estudio, categoria_estudio )['get_modelo']
        modelo.delete()
        
        data = {
                'valid':True
        }

        return JsonResponse(data)


#Obtenemos un modelo especifico y un formulario especifico 
def get_obj_form( id_estudio, categoria ):
        
        EMBARAZADA = {
                'model':Estudio_Embarazada,
                'form':formulario_estduio_embarazada,
        }
        HEPATOGRAMA = {
                'model':Estudio_Hepatograma,
                'form':formulario_estduio_hepatograma,
        }
        ORINA = {
                'model':Estudio_Orina,
                'form':formulario_estduio_orina,
        }
        UROCULTIVO = {
                'model':Estudio_Urocultivo,
                'form':formulario_estduio_urocultivo,
        }
        PROTEINOGRAMA = {
                'model':Estudio_Proteinograma,
                'form':formulario_estduio_proteinograma,
        }
        QUIMICA = {
                'model':Estudio_Quimica,
                'form':formulario_estduio_quimica,
        }
        CULTIVO = {
                'model':Estudio_Cultivo,
                'form':formulario_estduio_cultivo,
        }
        PARASITOLOGICO = {
                'model':Estudio_Parasitologico,
                'form':formulario_estduio_parasitologico,
        }
        HEMOGRAMA = {
                'model':Estudio_Hemograma,
                'form':formulario_estudio_hemograma,
        }
        GENERAL = {
                'model':Estudio_General,
                'form':formulario_estudio_general,
        }

        CATEGORIAS = {
                '0': EMBARAZADA,
                '1': HEPATOGRAMA,
                '2': ORINA,
                '3': UROCULTIVO,
                '4': PROTEINOGRAMA,
                '5': QUIMICA,
                '6': CULTIVO,
                '7': PARASITOLOGICO,
                '8': HEMOGRAMA,
                '9': GENERAL,
        }
        

       
        for clave, valor in CATEGORIAS.items():
            
                if categoria is clave:
                        obj = get_object_or_404( valor['model'], id = id_estudio )
                        form = valor['form']

        return { 'get_modelo':obj, 'get_formulario':form }

#Para mandarlos a JS codificados y luego separarlos por _ y **
def pasar_resultados_a_string( lista ):
        string = ''
        for i in lista:
                if len(lista[0]) > 2:
                        string += i[0] + '_'
                        string += i[1] + '_'
                        string += i[2] 
                        string += '**'
                else:
                        string += i[0] + '_'
                        string += i[1] + '_'
                        string += '**'

        return string

#Tabla de resultados del estudio
def resultados_del_estudio( estudio ):
        ####### definimos una parte de la tabla fija *****
        EMBARAZADA_REF = [
                '0,70 - 1,10 g/l',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
        ]

        HEPATOGRAMA_REF = [
                'Hasta 12 mU/ml',
                'Hasta 12 mU/ml',
                '68 a 240 | Niños: 100 a 400 mU/ml',
                'Hombres: 6 a 28 | Mujeres: 4 a 18',
                '-',
                '-',
                '-',
                'Hasta 120 mU/ml',
        ]

        ORINA_REF = [
                'A. Ambar',
                'Limpido',
                'Sui-Generis',
                'Blanca Fugaz',
                'Nulo Escaso',
                'Acida',
                '1010 - 1025',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
        ]

        UROCULTIVO_REF = [
                '-',
                '-',
                '-',
                '-',
        ]

        PROTEINOGRAMA_REF = [
                '6,50 a 7,90 g/dl',
                '3,50 a 4,80 g/dl',
                '0,25 + 0,08 g/dl',
                '0,64 + 0,11 g/dl',
                '0,71 + 0,20 g/dl',
                '1,26 + 0,42 g/dl',
                '-',
                '-',
        ]

        QUIMICA_REF = [
                '0,70 - 1,10 g/l',
                'Hasta 0,40 g/l',
                'Hasta 2,20 g/l',
                'Hasta 1,70 g/l',
                'Hombres: 30 a 60 | Mujeres: 20 a 50',
        ]

        CULTIVO_REF = [
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
        ]
        PARASITOLOGICO_REF = [
                '-',
                '-',
                '-',
                '-',
        ]

        HEMOGRAMA_REF = [
                '-',
                '-',
                '-',
                'F.Relativa: 3-5% | F.Absoluta: 140-450',
                'F.Relativa: 50-65% | F.Absoluta: 2500-5200',
                'F.Relativa: 2-4% | F.Absoluta: 50-320',
                'F.Relativa: 0-1% | F.Absoluta: 0-50',
                'F.Relativa: 25-35% | F.Absoluta: 1000-2800',
                'F.Relativa: 2-6% | F.Absoluta: 200-640',
                '-',
                'A.Ambar',
                'Limpido',
                'Sui.Generis',
                'Blanca Fugaz',
                'Nulo Escaso',
                'Acida',
                '1010 - 1025',
                '-',
                '-',
                '-',
                '-',
                '-',
                '-',
        ]

        GENERAL_REF = [
                '-',
                '-',
                
        ]



        CATEGORIAS = {
                'embarazada':0,
                'hepatograma':1,
                'orina':2,
                'urocultivo':3,
                'proteinograma':4,
                'quimica':5,
                'cultivo':6,
                'parasitologico':7,
                'hemograma':8,
                'general':9
        }

        VALORES_REF = {
                'embarazada': EMBARAZADA_REF,
                'hepatograma': HEPATOGRAMA_REF,
                'orina': ORINA_REF,
                'urocultivo': UROCULTIVO_REF,
                'proteinograma': PROTEINOGRAMA_REF,
                'quimica': QUIMICA_REF,
                'cultivo': CULTIVO_REF,
                'parasitologico': PARASITOLOGICO_REF,
                'hemograma':HEMOGRAMA_REF,
                'general':GENERAL_REF,
        }

        #Diccionary: Guardamos las propiedades del objeto en un diccionario clave valor
        for ver in estudio:
                categoria_estudio = ver.categoria #int: La usamos luego para hacer una condicion
                estudio_dict = ver.__dict__ #Diccionario 

        #Array: Guardamos solo los keys del diccionario
        keys = []
        for i in estudio_dict.keys():
                keys.append( i.replace('_', ' ').capitalize() )

        #Array: Guardamos solo los values del diccionario
        values = []
        for i in estudio_dict.values():
                values.append( i )

        #Array: Guardamos algunos keys, values e info extra
        keys_and_values = []
        CATEGORIA = 1
        RESULTADOS = 4

        start = 0 #Es una mouseherramienta que nos ayudara mas tarde( para un bucle )
        
        #Bucle: Rellenamos la lista keys_and_values con toda la info que necesitamos
        for i in range( len(values) ):
                if i is CATEGORIA:
                        for clave in CATEGORIAS:
                                if categoria_estudio is CATEGORIAS[clave]:
                                        valores_de_referencia = VALORES_REF[clave] 
                 
                if i > RESULTADOS:
                        
                        
                        for valor in range( start, len(valores_de_referencia) ):
                               
                                if categoria_estudio == 9: #Categoria General
                                        keys_and_values.append( [
                                                keys[i],
                                                values[i]
                                                
                                        ])
                                        print( 'aqui' )
                                else:
                                        keys_and_values.append( [
                                                keys[i],
                                                values[i],
                                                valores_de_referencia[valor]    
                                        ])
                                        print( 'aqui2' )
                                break
                        start += 1

        
        #Array: Para luego obtener cada una de las propiedades en la pantalla 
        return keys_and_values

def observacion_estudio( estudio ):
        observacion = None
        try:
                for ver in estudio:
                        observacion = ver.observaciones
                
                if observacion is None:
                        observacion = 'ninguna'
        
        except AttributeError:
                print('El estudio GENERAL no tiene la columna observaciones')

        return observacion

def nuevo_estudio( request, categoria ):
        ESTUDIOS = {
                '0':{
                        'nombre_estudio':'embarazada',
                        'formulario':formulario_estduio_embarazada
                },
                '1':{
                        'nombre_estudio':'hepatograma',
                        'formulario':formulario_estduio_hepatograma
                },
                        
                '2':{
                        'nombre_estudio':'orina',
                        'formulario':formulario_estduio_orina
                },
                        
                '3':{
                        'nombre_estudio':'urocultivo',
                        'formulario':formulario_estduio_urocultivo,
                },
                        
                '4':{
                        'nombre_estudio':'proteinograma',
                        'formulario':formulario_estduio_proteinograma,
                },
                '5':{
                        'nombre_estudio':'quimica',
                        'formulario':formulario_estduio_quimica,
                },
                        
                '6':{
                        'nombre_estudio':'cultivo',
                        'formulario':formulario_estduio_cultivo,
                },
                        
                '7':{
                        'nombre_estudio':'parasitologico',
                        'formulario':formulario_estduio_parasitologico,
                },
                        
                '8':{
                        'nombre_estudio':'hemograma',
                        'formulario':formulario_estudio_hemograma,
                },
                '9':{
                        'nombre_estudio':'general',
                        'formulario':formulario_estudio_general,
                }
                        

        }

        formulario_elegido = ESTUDIOS[categoria]['formulario']
        template_html = 'formularios/estudio_'+ ESTUDIOS[categoria]['nombre_estudio'] + '.html'

        if request.method == 'POST':
                form = formulario_elegido(request.POST)
                data = None
                print(form)

                if form.is_valid():
                        form.save()
                        
                data = {
                        'valid':form.is_valid()
                }

                return JsonResponse(data)
        
        else:
                form = formulario_elegido

        contexto = {'form':form}

        return render( request, template_html , contexto)


'''
class estudio_embarazada( CreateView ):
        model = Estudio_Embarazada
        form_class = formulario_estduio_embarazada
        template_name = 'formularios/estudio_embarazada.html'
        success_url = '/'
'''

def nueva_caratula( request ):
        form = formulario_nueva_caratula
        return render( request, 'formularios/nueva_caratula.html', {'form':form})
