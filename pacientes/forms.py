from django import forms

from .models import Paciente

class formulario_nuevo_paciente_principal( forms.ModelForm ):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'dni', 'celular')

        labels = {}
        for i in fields:
            labels[i] = i.capitalize()

        widgets = {
            'nombre': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder':'Nombre',

                            }
                        ),

            'apellido': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'Apellido',
                            }
                        ),

            'dni': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'DNI',
                                'max':10,
                                'min':10,
                                'type':'number',
                                'onChange':'buscarPaciente( "en_nuevo_paciente" )',
                            }
                        ),

            'celular': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'Celular',
                                'type':'number',
                            }
                        ),
            
            'direccion': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'Direccion',
                            }
                        ),
            
            'sexo': forms.Select( 
                            attrs={
                                'class':'form-control',
                            }
                        )
        }


class formulario_nuevo_paciente_modal( forms.ModelForm ):
    class Meta:
        model = Paciente
        fields = ('nombre', 'apellido', 'dni', 'celular')

        widgets = {
            'nombre': forms.TextInput(
                            attrs={
                                'class':'form-control',
                                'placeholder':'Nombre',

                            }
                        ),

            'apellido': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'Apellido',
                            }
                        ),

            'dni': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'DNI',
                                'max':'10',
                                'min':'10',
                                'type':'number',
                                'onChange':'buscarPaciente2()',
                            }
                        ),

            'celular': forms.TextInput( 
                            attrs={
                                'class':'form-control',
                                'placeholder':'Celular',
                                'type':'number',
                            }
                        ),
            
        }
        
            
