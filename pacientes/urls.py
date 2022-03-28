from django.urls import path, include

from .views import paciente_nuevo_modal, nuevo_paciente, ver_paciente, pacientes, \
    editar_paciente,eliminar_paciente, confirmar_eliminacion_paciente, ajax_get_view, ver_todos_los_pacientes, ver_todos_filtro, not_fund

app_name = 'pacientes'

urlpatterns = [
    path('', pacientes, name='pacientes_' ),
    path('nuevo/', nuevo_paciente, name='nuevo_paciente' ),
    path('nuevo_modal/', paciente_nuevo_modal, name='nuevo_paciente_modal' ),
    path('ver/<pk>', ver_paciente.as_view(), name='ver_paciente' ),
    path('editar/<pk>/', editar_paciente, name='editar_paciente' ),
    path('eliminar/<pk>/', eliminar_paciente, name='eliminar_paciente' ),
    path('confirmar_eliminacion/', confirmar_eliminacion_paciente, name='confirm_eliminacion_paciente' ),
    path('ver_todos/', ver_todos_los_pacientes.as_view(), name='ver_todos_los_pacientes' ),
    path('ver_todos_filtro/', ver_todos_filtro, name='ver_todos_filtro' ),
    path('buscar2/', ajax_get_view, name='buscar_paciente_2' ),
    path('404/', not_fund, name='404' ),
]
