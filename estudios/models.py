from django.db import models

from pacientes.models import Paciente

class Estudio_General( models.Model ):
    categoria = models.IntegerField( default= 9 )

    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    #Material examinado
    analisis_solicitado = models.CharField( max_length= 200)
    detalle = models.CharField( max_length= 200 )


    def __str__( self ):
        return 'General'

    class Meta:
        verbose_name = 'General'
        verbose_name_plural = 'Generales'

class Estudio_Hemograma( models.Model ):
    categoria = models.IntegerField( default= 8 )

    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    #Material examinado
    hematies = models.CharField( max_length= 200)
    hematocrito = models.CharField( max_length= 200)
    leucocitos = models.CharField( max_length= 200)

    #formula leucocitaria
    neutrofilos_en_cayado = models.CharField( max_length= 200)
    neutrofilos_segmentados = models.CharField( max_length= 200)
    eosinofilos = models.CharField( max_length= 200)
    basofilos = models.CharField( max_length= 200)
    linfocitos = models.CharField( max_length= 200)
    monocitos = models.CharField( max_length= 200)

    observaciones_1 = models.CharField( max_length=500, default='Ninguna' )


    color = models.CharField( max_length=200)
    aspecto = models.CharField( max_length=200)
    olor = models.CharField( max_length=200)
    espuma = models.CharField( max_length=200)
    sedimento = models.CharField( max_length=200)
    reaccion = models.CharField( max_length=200)
    densidad = models.CharField( max_length=200)
    albumina = models.CharField( max_length=200)
    glucosa = models.CharField( max_length=200)
    c_cetonicos = models.CharField( max_length=200)
    pig_bilares = models.CharField( max_length=200)
    s_bilares = models.CharField( max_length=200)
    urobilina = models.CharField( max_length=200)

    observaciones = models.CharField( max_length=9000, null=True, blank=True )


    def __str__( self ):
        return 'Hemograma'

    class Meta:
        verbose_name = 'Hemograma'
        verbose_name_plural = 'Hemogramas'


class Estudio_Embarazada( models.Model ):
    categoria = models.IntegerField( default=0) 
       
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    glucemia = models.CharField( max_length=200 )
    gurpo_sanguineo = models.CharField( max_length=200 )
    factor_rh = models.CharField( max_length=200 )
    vdrl = models.CharField( max_length=200 )
    hai_chagas = models.CharField( max_length=200 )
    tif_chagas = models.CharField( max_length=200 )
    tif_toxoplasmosis = models.CharField( max_length=200 )
    antic_anti_hiv = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )

        
    def __str__( self ):
        return 'Embarazo'

    class Meta:
        verbose_name = 'Embarazada'
        verbose_name_plural = 'Embarazadas'

class Estudio_Hepatograma( models.Model ):
    categoria = models.IntegerField( default=1) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    transaminasa_glutamico_piruvica = models.CharField( max_length=200 )
    transaminasa_glutamico_oxalacetica = models.CharField( max_length=200 )
    fosfata_alcaina = models.CharField( max_length=200 )
    gamma_glutamil_tanspeptidasa = models.CharField( max_length=200 )
    bilirrubina_total = models.CharField( max_length=200 )
    bilirrubina_directa = models.CharField( max_length=200 )
    bilirrubina_indirecta = models.CharField( max_length=200 )
    amilasemia = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )



        
    def __str__( self ):
        return 'Hepatograma'

    class Meta:
        verbose_name = 'Hepatograma'
        verbose_name_plural = 'Hepatogramas'

class Estudio_Orina( models.Model ):
    categoria = models.IntegerField( default=2) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    color= models.CharField( max_length=200 )
    aspecto = models.CharField( max_length=200 )
    olor = models.CharField( max_length=200 )
    espuma = models.CharField( max_length=200 )
    sedimento = models.CharField( max_length=200 )
    reaccion = models.CharField( max_length=200 )
    densidad = models.CharField( max_length=200 )

    albumina= models.CharField( max_length=200 )
    glucosa = models.CharField( max_length=200 )
    c_catonicos = models.CharField( max_length=200 )
    pig_bilares = models.CharField( max_length=200 )
    s_bilares = models.CharField( max_length=200 )
    robilina = models.CharField( max_length=200 )
    hemoglobina = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )





        
    def __str__( self ):
        return 'Orina'

    class Meta:
        verbose_name = 'Orina'
        verbose_name_plural = 'Orinas'

class Estudio_Urocultivo( models.Model ):
    categoria = models.IntegerField( default=3) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    examen_directo= models.CharField( max_length=200 )
    examen_seriado = models.CharField( max_length=200 )
    enriquesimiento = models.CharField( max_length=200 )
    material_examinado = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )



    

        
    def __str__( self ):
        return 'Urocultivo'

    class Meta:
        verbose_name = 'Urocultivo'
        verbose_name_plural = 'Urocultivos'

class Estudio_Proteinograma( models.Model ):
    categoria = models.IntegerField( default=4) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    proteinas_totales= models.CharField( max_length=200 )
    albumina = models.CharField( max_length=200 )
    olor = models.CharField( max_length=200 )
    alfa1_globulinas = models.CharField( max_length=200 )
    alfa2_globulinas = models.CharField( max_length=200 )
    betta_globulinas = models.CharField( max_length=200 )
    gamma_glubolinas = models.CharField( max_length=200 )
    globulinas = models.CharField( max_length=200 )
    relacion_ag  = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )





        
    def __str__( self ):
        return 'Proteinograma'

    class Meta:
        verbose_name = 'Proteinograma'
        verbose_name_plural = 'Proteinogramas'

class Estudio_Quimica( models.Model ):
    categoria = models.IntegerField( default=5) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    glucemia= models.CharField( max_length=200 )
    uremia = models.CharField( max_length=200 )
    colesterolemia = models.CharField( max_length=200 )
    trigliceridemia = models.CharField( max_length=200 )
    uricemia = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )





        
    def __str__( self ):
        return 'Quimica'

    class Meta:
        verbose_name = 'Quimica'
        verbose_name_plural = 'Quimicas'

class Estudio_Cultivo( models.Model ):
    categoria = models.IntegerField( default=6) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    sedimiento_urianario= models.CharField( max_length=200 )
    cultivo = models.CharField( max_length=200 )
    recuento_de_colonias = models.CharField( max_length=200 )
    germen_identificatorio = models.CharField( max_length=200 )
    antiobiograma = models.CharField( max_length=200 )
    sensisble_a = models.CharField( max_length=200 )
    resitente_a = models.CharField( max_length=200 )
    

    observaciones = models.CharField( max_length=9000, null=True, blank=True )

        
    def __str__( self ):
        return 'Urocultivo'

    class Meta:
        verbose_name = 'Cultivo'
        verbose_name_plural = 'Cultivo'

class Estudio_Parasitologico( models.Model ):
    categoria = models.IntegerField( default=7) 
    paciente = models.ForeignKey( Paciente, on_delete=models.CASCADE )
    fecha_estudio = models.DateTimeField( auto_now_add=True )

    examen_directo= models.CharField( max_length=200 )
    examen_seriado = models.CharField( max_length=200 )
    enriquesimiento = models.CharField( max_length=200 )
    material_examinado = models.CharField( max_length=200 )

    observaciones = models.CharField( max_length=9000, null=True, blank=True )



        
    def __str__( self ):
        return 'Parasitologico'

    class Meta:
        verbose_name = 'Parasitologico'
        verbose_name_plural = 'Parasitologicos'