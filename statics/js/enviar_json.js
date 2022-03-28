function enviar_formulario( lugar, tipo , id_formulario, categoria_formulario, id, categoria ){ // Lugar: 'Paciente' o 'Estudio'
                                                            // Tipo: 'creacion' o 'edicion'
                                                           // ID: del formulario  
    let formulario;
    
    if( id_formulario != '' ){
        formulario = new FormData( document.getElementById(id_formulario) );
       
    }
   
    let url = `../../../${lugar}/`
    
    switch( tipo ){
        case 'creacion':{
            if(lugar == 'paciente'){
                url += `nuevo/`
            }

            if( lugar == 'estudio'){

                url += `nuevo_estudio/${categoria_formulario}/`
            }
            
            break;
        }

        case 'edicion':{

            if(lugar == 'paciente'){
                url += `editar/${id}/`
            }

            if( lugar == 'estudio'){
                url += `editar/${id}/${categoria}/`
            }

            break;
        }

        case 'eliminacion':{
           
            if(lugar == 'paciente'){
                url += `confirmar_eliminacion/`
                

                formulario = JSON.stringify( { elemento:id} );
            }

            if( lugar == 'estudio'){
                url += `confirmar_eliminacion_estudio/`

                formulario = JSON.stringify( { elemento:categoria, elemento2:categoria_formulario} );
            }

            
            
            break;
        }
    }
    const csrf_token = getCookie('csrftoken');

    fetch( url, {
      method: 'POST',
      body: formulario,
      headers: {
          "X-CSRFToken": csrf_token 
      }
    })

    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {
      if( data['valid'] ) success(lugar, tipo,  id, id_formulario);
      else alert('Algo salio mal')
    })
}

function success( lugar, tipo, id, id_formulario ){
    let cambio;
    let alerta = document.getElementById('alerta');

    alerta.setAttribute('style','display:block');

    let remover = window.setInterval( function(){
        alerta.setAttribute('style','display:none')
        clearInterval(remover)
        
    }, 3000 )

    switch( lugar ){
        case 'paciente':{
            if( tipo == 'creacion'){
                alerta.innerHTML = '¡Paciente creado con éxito! <i class="far fa-thumbs-up"></i>'

                if( id_formulario == 'formulario_nuevo_paciente' ){
                    $('#nuevo_paciente').modal('hide');
                    buscarPaciente('en_formulario_estudios');
                } else {
                    contenedor_elegido = 'nuevo_paciente'
                    cambio = window.setInterval( function(){
                    cambiarContenedor( contenedor_elegido, id )
                    clearInterval(cambio)
                    }, 150 )
                }


            }if( tipo == 'edicion') {
                alerta.innerHTML = '¡Paciente editado con éxito! <i class="far fa-thumbs-up"></i>'
                
                contenedor_elegido = 'ver_paciente'
                cambio = window.setInterval( function(){
                    cambiarContenedor( contenedor_elegido, id )
                    clearInterval(cambio)
                }, 150 )

                $('#modal_editar').modal('hide')

                cambio;
                

                

            }if( tipo == 'eliminacion') {
                alerta.innerHTML = '¡Paciente eliminado con éxito! <i class="far fa-thumbs-up"></i>'
                
                contenedor_elegido = 'ver_pacientes'
                cambio = window.setInterval( function(){
                    cambiarContenedor( contenedor_elegido )
                    clearInterval(cambio)
                }, 150 )

               

                $('#modal_eliminar').modal('hide')
                cambio;

                
            }
            
            break;
        }

        case 'estudio':{
            if( tipo == 'creacion'){
                alerta.innerHTML = '¡Estudio creado con éxito! <i class="far fa-thumbs-up"></i>'
                
                cambio = window.setInterval( function(){
                    window.location.href = 'http://' +window.location.host + '/estudio/'
                    clearInterval(cambio)
                }, 140 )
                
                cambio;
            }
            if( tipo == 'edicion'){
                alerta.innerHTML = '¡Estudio editado con éxito! <i class="far fa-thumbs-up"></i>'
                id = document.getElementById('id_paciente').value;
                contenedor_elegido = 'ver_paciente'
                cambio = window.setInterval( function(){
                    cambiarContenedor( contenedor_elegido, id )
                    clearInterval(cambio)
                }, 150 )

                cambio;

                $('#modal_editar_estudio').modal('hide')
            }
            if( tipo == 'eliminacion') {
                alerta.innerHTML = '¡Etudio eliminado con éxito! <i class="far fa-thumbs-up"></i>'
                contenedor_elegido = 'ver_paciente' 
                cambio = window.setInterval( function(){
                    cambiarContenedor( contenedor_elegido, id )
                    clearInterval(cambio)
                }, 150 )

                cambio;

                $('#modal_eliminar_estudio').modal('hide')
            }
            break;
        }

        
    }
   
    remover;
    
    
    
    
    
    

}




function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}