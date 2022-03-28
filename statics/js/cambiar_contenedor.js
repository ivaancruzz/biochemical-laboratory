var contenedor = document.getElementById('contenedor_dinamico');
//var dni = document.getElementById('dni').values;
var url = null;
var option_anterior;


function cambiarContenedor( calbk , dni ){
    
        switch( calbk ){
            //Zona pacientes
            case 'nuevo_paciente': cont_nuevo_paciente(); break;
            case 'ver_pacientes': cont_ver_pacientes(); break;
            case 'ver_resultado_busqueda': cont_resultado_busqueda(dni); break;
            case 'ver_paciente': ver_paciente( dni ); break;
            case 'eliminar_paciente': eliminar_paciente( dni ); break;
            case 'editar_paciente': editar_paciente( dni ); break;
            case 'ordenar_fecha': ordenar_por( 'fecha' ); break;
            case 'ordenar_nombre': ordenar_por( 'nombre' ); break;
            case 'ordenar_apellido': ordenar_por( 'apellido' ); break;

            //Zona Estudios
            case 'estudios': estudios(); break;
            case 'nueva_caratula': nueva_caratula(); break;
            case 'hemograma': nuevo_estudio('8'); break;
            case 'embarazada': nuevo_estudio('0'); break;
            case 'hepatograma': nuevo_estudio('1'); break;
            case 'orina': nuevo_estudio('2'); break;
            case 'urocultivo': nuevo_estudio('3'); break;
            case 'proteinograma': nuevo_estudio('4'); break;
            case 'quimica': nuevo_estudio('5'); break;
            case 'cultivo': nuevo_estudio('6'); break;
            case 'parasitologico': nuevo_estudio('7'); break;
            case 'general': nuevo_estudio('9'); break;
        }

}

tippy('#ver_pacientes', {
    content: 'Ver pacientes registrados',
});

tippy('#crear_paciente', {
    content: 'Registrar paciente',
});

tippy('#buscar', {
    content: 'Buscar',
});



function cont_nuevo_paciente( ){
    url = '../../paciente/nuevo/';
    $('#contenedor_dinamico').load( url )
}

function cont_ver_pacientes( ){
    url = '../../paciente/ver_todos_filtro/';
    $('#contenedor_dinamico').load( url )
}



function cont_resultado_busqueda( dni ){
    url = '../../paciente/ver/'+dni;
    $('#contenedor_dinamico').load( url )
}

function editar_paciente( dni ){
    url = '../../paciente/editar/'+dni;
    $('#modal_editar').load( url , function(){
        $(this).modal('show');
                
    })
}

function eliminar_paciente( dni ){
    url = '../../paciente/eliminar/'+dni;
    $('#modal_eliminar').load( url , function(){
        $(this).modal('show');
                
    })
}

function ver_paciente( dni, lugar ){
    
   
    url = '../../paciente/ver/'+dni;
    $('#contenedor_dinamico').load( url )
    
    
}

function ordenar_por( valor ){  
    switch(valor){
        case 'fecha': {
            url = '../../paciente/ver_todos/?ordering=-fecha_registro';
            break;
        }
        case 'nombre': {
            url = '../../paciente/ver_todos/?ordering=nombre';
            break;
        }
        case 'apellido': {
            url = '../../paciente/ver_todos/?ordering=apellido';
            break;
        }
    }
    
    $('#mostrar_tabla').load( url )
    
}

function estudios(){
    url = '../../estudio/';
    $('#contenedor_dinamico').load( url )
}

function nueva_caratula(){
    url = '../../estudio/nueva_caratula/';
    $('#contenedor_dinamico_estudios').load( url )
}

function nuevo_estudio( categoria ){
    url = '../../estudio/nuevo_estudio/'+categoria+'/';
    $('#contenedor_dinamico_estudios').load( url )
}
