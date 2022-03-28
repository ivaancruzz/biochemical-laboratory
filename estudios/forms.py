from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit

from .models import Estudio_Hemograma, Estudio_Embarazada, Estudio_Hepatograma, Estudio_Orina, Estudio_Urocultivo, \
        Estudio_Proteinograma, Estudio_Quimica, Estudio_Cultivo, Estudio_Parasitologico, Estudio_General

class formulario_estudio_general( forms.ModelForm ):
    class Meta:
        model = Estudio_General
        
        fields = (
            'paciente', 'analisis_solicitado', 
            'detalle',
        )
        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:

            if w == 'detalle':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })
            elif w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'DNI del paciente',
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'style': 'font-size: 12px',
                    
                })

            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px',
                })

            labels[w] = w.replace('_', ' ').capitalize() + ': '


            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-general'}
        self.helper.layout = Layout(
            Row(
                Column('analisis_solicitado', css_class='form-group col-md-6 mb-6  border-bottom'),
                Column('paciente', css_class='form-group col-md-6 mb-6  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                
                Column('detalle', css_class='form-group col-md-12 mb-6 border-bottom')

            )
            

        )


class formulario_estudio_hemograma( forms.ModelForm ):
    class Meta:
        model = Estudio_Hemograma
        
        fields = (
            'paciente', 'hematies', 
            'hematocrito', 
            'leucocitos', 
            'neutrofilos_en_cayado',
            'neutrofilos_segmentados','eosinofilos',
            'basofilos','linfocitos', 'monocitos',
            'observaciones_1',
 
            'color',
            'aspecto','olor',
            'espuma','sedimento', 'reaccion',
            'densidad','albumina',
            'glucosa','c_cetonicos', 'pig_bilares',
            's_bilares','urobilina',

            'observaciones',
            
            )

        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:
            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {  
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )
            
            elif w == 'observaciones_1':
                widgets[w] = forms.TextInput( attrs= {  
                    'placeholder':'Escribe algo...',
                    'style': 'font-size: 12px',
                } )
                labels[w] = 'Observaciones: '



            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })
       
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '


            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-hemograma'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('hematies', css_class='form-group col mb-3  border-bottom border-bottom'),
                Column('hematocrito', css_class='form-group col mb-3 border-bottom border-bottom'),
                Column('leucocitos', css_class='form-group col mb-3 border-bottom border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('neutrofilos_en_cayado', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('neutrofilos_segmentados', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('eosinofilos', css_class='form-group col-md-3 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('basofilos', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('linfocitos', css_class='form-group col mb-3 border-bottom'),
                Column('monocitos', css_class='form-group col mb-3 border-bottom'),
                css_class = 'form-row'
            ),
            Row(
                Column('observaciones_1', css_class='form-group col mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),


            Row(
                Column('color', css_class='form-group col mb-3 border-bottom'),
                Column('aspecto', css_class='form-group col mb-3 border-bottom'),
                Column('olor', css_class='form-group col mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),
            Row(
                Column('espuma', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('sedimento', css_class='form-group col mb-3 border-bottom'),
                Column('reaccion', css_class='form-group col mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('densidad', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('albumina', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('glucosa', css_class='form-group col mb-3 border-bottom'),
                css_class = 'form-row'
            ),
            Row(
                
                Column('c_cetonicos', css_class='form-group col mb-3 border-bottom'),
                Column('pig_bilares', css_class='form-group col mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),
            Row(
                
                Column('s_bilares', css_class='form-group col mb-0 mb-3  border-bottom'),
                Column('urobilina', css_class='form-group col mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )

    

class formulario_estduio_hepatograma( forms.ModelForm ):
    class Meta:
        model = Estudio_Hepatograma
        
        fields = (
            'paciente', 'transaminasa_glutamico_piruvica', 
            'transaminasa_glutamico_oxalacetica', 
            'fosfata_alcaina', 
            'gamma_glutamil_tanspeptidasa',
            'bilirrubina_total','bilirrubina_directa',
            'bilirrubina_indirecta','amilasemia',
            'observaciones',
            )

        help_texts = {}
        labels = {}
        widgets = {}

        for w in fields:
            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )

                help_texts[w] = 'Ingrese un DNI registrado'

            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })


                
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '

                help_texts[w] = 'mU/ml'

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-hepatograma'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('transaminasa_glutamico_piruvica', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('transaminasa_glutamico_oxalacetica', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('fosfata_alcaina', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('gamma_glutamil_tanspeptidasa', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('bilirrubina_total', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('bilirrubina_directa', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('bilirrubina_indirecta', css_class='form-group col-md-6 mb-0'),
                Column('amilasemia', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='mb-3 border-bottom'),
                
            ),
            

        )

    
    
class formulario_estduio_embarazada( forms.ModelForm ):
    class Meta:
        model = Estudio_Embarazada
        fields = (
            'paciente', 'glucemia', 
            'gurpo_sanguineo', 
            'factor_rh', 'vdrl',
            'hai_chagas','tif_chagas',
            'tif_toxoplasmosis','antic_anti_hiv',
            'observaciones'
            )
        
        help_texts = { 'glucemia': 'g/l'}
        labels = {}
        widgets = {}

        for w in fields:
            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )
                help_texts[w] = 'Ingrese un DNI registrado'
            
            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

            
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-embarazada'}
        self.helper.layout = Layout(


            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('glucemia', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('gurpo_sanguineo', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('factor_rh', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('vdrl', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('hai_chagas', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('tif_chagas', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('tif_toxoplasmosis', css_class='form-group col-md-6 mb-0'),
                Column('antic_anti_hiv', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),

        )


class formulario_estduio_orina( forms.ModelForm ):
    class Meta:
        model = Estudio_Orina
        fields = (
            'paciente', 'color', 
            'aspecto', 'olor', 
            'espuma','sedimento',
            'reaccion','densidad',
            'albumina','glucosa',
            'c_catonicos','pig_bilares',
            's_bilares','robilina','hemoglobina',
            'observaciones'
            )

        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:
            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )


            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })
               
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder':'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-orina'}
        self.helper.layout = Layout(


            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('color', css_class='form-group col-md-4 mb-3  border-bottom'),
                Column('aspecto', css_class='form-group col-md-4 mb-3 border-bottom'),
                Column('olor', css_class='form-group col-md-4 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                
                Column('espuma', css_class='form-group col-md-4 mb-0 mb-3  border-bottom'),
                Column('sedimento', css_class='form-group col-md-4 mb-0 mb-3  border-bottom'),
                Column('reaccion', css_class='form-group col-md-4 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('densidad', css_class='form-group col-md-4 mb-0'),
                Column('albumina', css_class='form-group col-md-4 mb-0'),
                Column('glucosa', css_class='form-group col-md-4 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('c_catonicos', css_class='form-group col-md-4 mb-0'),
                Column('pig_bilares', css_class='form-group col-md-4 mb-0'),
                Column('s_bilares', css_class='form-group col-md-4 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('robilina', css_class='form-group col-md-6 mb-0'),
                Column('hemoglobina', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )

class formulario_estduio_urocultivo( forms.ModelForm ):
    class Meta:
        model = Estudio_Urocultivo
        fields = (
            'paciente','examen_directo', 'examen_seriado', 
            'enriquesimiento', 'material_examinado',
            'observaciones'
            )

        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:
            if w  == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )
            
            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

                
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-urocultivo'}
        self.helper.layout = Layout(


            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('examen_directo', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('examen_seriado', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('enriquesimiento', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('material_examinado', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )

class formulario_estduio_proteinograma( forms.ModelForm ):
    class Meta:
        model = Estudio_Proteinograma
        fields = (
            'paciente','proteinas_totales', 'albumina', 
            'olor', 'alfa1_globulinas', 
            'alfa2_globulinas','betta_globulinas',
            'gamma_glubolinas','globulinas', 'relacion_ag',
            'observaciones'
            )
        
        help_texts = {}
        labels = {}
        widgets = {}

        for w in fields:
            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )

                help_texts[w] = 'Ingrese un DNI registrado'

            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })
                
            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

                labels[w] = w.replace('_', ' ').capitalize() + ': '

                help_texts[w] = 'g/dl'

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-proteinograma'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('proteinas_totales', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('albumina', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('olor', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('alfa1_globulinas', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('alfa2_globulinas', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('betta_globulinas', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('gamma_glubolinas', css_class='form-group col-md-6 mb-0'),
                Column('globulinas', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('relacion_ag', css_class='form-group col-md-6 mb-0'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )

class formulario_estduio_quimica( forms.ModelForm ):
    class Meta:
        model = Estudio_Quimica
        fields = (
            'paciente','glucemia', 'uremia', 
            'colesterolemia', 'trigliceridemia', 
            'uricemia', 'observaciones'
            )
        help_texts = {}
        labels = {}
        widgets = {}

        for w in fields:
            labels[w] = w.replace('_', ' ').capitalize() + ': '

            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )

                help_texts[w] = 'Ingrese un DNI registrado'

            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

               

                help_texts[w] = 'g/l'

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-quimica'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('glucemia', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('uremia', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('colesterolemia', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('trigliceridemia', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('uricemia', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
               
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),

            

        )

class formulario_estduio_cultivo( forms.ModelForm ):
    class Meta:
        model = Estudio_Cultivo
        fields = (
            'paciente','sedimiento_urianario', 'cultivo', 
            'recuento_de_colonias', 'germen_identificatorio', 
            'antiobiograma','sensisble_a',
            'resitente_a', 'observaciones'
            )
        help_texts = {}
        labels = {}
        widgets = {}

        for w in fields:
            labels[w] = w.replace('_', ' ').capitalize() + ': '

            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )
                help_texts[w] = 'Ingrese un DNI registrado'


            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })

               

                help_texts[w] = 'g/l'

            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-cultivo'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('sedimiento_urianario', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('cultivo', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('recuento_de_colonias', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('germen_identificatorio', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('antiobiograma', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('sensisble_a', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('resitente_a', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),

            

        )

class formulario_estduio_parasitologico( forms.ModelForm ):
    class Meta:
        model = Estudio_Parasitologico
        fields = (
            'paciente','examen_directo', 'examen_seriado', 
            'enriquesimiento', 'material_examinado', 'observaciones'
            )
        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:
            labels[w] = w.replace('_', ' ').capitalize() + ': '

            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )

            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })


            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-parasitologico'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('examen_directo', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('examen_seriado', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('enriquesimiento', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('material_examinado', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),
            
            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )


class formulario_nueva_caratula( forms.Form ):
    class Meta:
        fields = (
            'paciente','examen_directo', 'examen_seriado', 
            'enriquesimiento', 'material_examinado', 'observaciones'
            )
        help_texts = {'paciente':'Ingrese un DNI registrado'}
        labels = {}
        widgets = {}

        for w in fields:
            labels[w] = w.replace('_', ' ').capitalize() + ': '

            if w == 'paciente':
                widgets[w] = forms.TextInput( attrs= {
                    'onChange':'buscarPaciente("en_formulario_estudios")',
                    'placeholder':'DNI del paciente',
                    'style': 'font-size: 12px',
                } )

            elif w == 'observaciones':
                widgets[w] = forms.Textarea( attrs= {
                    'placeholder': 'Escribe algo...',
                    'style': 'font-size: 12px', 
                })

            else:
                widgets[w] = forms.TextInput( attrs= {
                    'placeholder': 'Resultado...',
                    'style': 'font-size: 12px',
                })


            
    
    def __init__( self, *args, **kwargs ):
        super().__init__( *args, **kwargs )
        self.helper = FormHelper()
        self.helper.attrs = {'id':'form-id-parasitologico'}
        self.helper.layout = Layout(
            Row(
                Column('paciente', css_class='mb-3 border-bottom')
            ),

            Row(
                Column('examen_directo', css_class='form-group col-md-6 mb-3  border-bottom'),
                Column('examen_seriado', css_class='form-group col-md-6 mb-3 border-bottom'),
                css_class = 'form-row'
            ),

            Row(
                Column('enriquesimiento', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                Column('material_examinado', css_class='form-group col-md-6 mb-0 mb-3  border-bottom'),
                css_class = 'form-row'
            ),
            
            Row(
                Column('observaciones', css_class='form-group col mb-3  border-bottom'),
                
                css_class = 'form-row'
            ),
            

        )

