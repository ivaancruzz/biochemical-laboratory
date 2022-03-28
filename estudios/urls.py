from django.urls import path, include

from .views import estudios_page, \
                nueva_caratula, \
                nuevo_estudio, \
                ver_estudio, \
                editar_estudio, \
                eliminar_estudio, \
                confirm_eliminacion_estudio

app_name = 'estudios'
urlpatterns = [
    path('', estudios_page, name='estudios_' ),


    path('nuevo_estudio/<categoria>/', nuevo_estudio, name='nuevo_estudio' ),
    path('nueva_caratula/', nueva_caratula, name='nueva_caratula' ),
    path('ver/<id_estudio>/<categoria>/<paciente_id>/', ver_estudio, name='ver_estudio' ),
    path('editar/<id_estudio>/<categoria>/', editar_estudio, name='editar_estudio' ),
    path('eliminar/<id_estudio>/<categoria>/', eliminar_estudio, name='eliminar_estudio' ),
    path('confirmar_eliminacion_estudio/', confirm_eliminacion_estudio, name='confirm_eliminar_estudio' ),

]
