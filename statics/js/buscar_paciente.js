function buscarPaciente( lugar ){
    
    var elemento;
    if( lugar == 'en_formulario_estudios' ){
            elemento = document.getElementById('id_paciente').value;
            
            
    }

    if( lugar == 'en_nuevo_paciente' ){
        elemento = document.getElementById('id_dni').value;
        var btn = document.getElementById('btn-enviar');
        var small = document.getElementById('dni_small');
        
    }

    if( lugar == 'en_buscar_paciente' ){
            elemento = document.getElementById('dni').value;
            
    }
   

    const csrf_token = getCookie('csrftoken');

    
    fetch( "/paciente/buscar2/", {
        method: 'POST',
        body: JSON.stringify( { elemento:elemento} ),
        headers: {
            "X-CSRFToken": csrf_token 
        }
        
    })
    .then(response => {
        return response.json() //Convert response to JSON
    })
    .then(data => {
       
        mostrarMensaje( data['dni'], data['paciente_nombre'], lugar )
        
    })
    
    function mostrarMensaje( valor, paciente, lugar  ){
        if( valor == false ){

            if( lugar == 'en_nuevo_paciente' ){
                btn.removeAttribute('disabled', '')
                small.style.display = 'none'
                small.innerHTML = ''
            }


            if( lugar == 'en_formulario_estudios'){
                let get_small = document.getElementById('hint_id_paciente');
                get_small.innerHTML = 'Ingrese un DNI registrado';
                
                const url = '../../paciente/nuevo_modal/';

                $('#nuevo_paciente').load( url , function(){
                    $(this).modal('show');
                    
                })
            }

            if( lugar == 'en_buscar_paciente'){
                cambiarContenedor('ver_resultado_busqueda', elemento);
            }
            
            
            
        } else {
            if( lugar == 'en_nuevo_paciente' ){
                small.style.display = 'block'
                small.innerHTML = 'Este DNI ya esta registrado'
                btn.setAttribute('disabled', '')
                
            }

            if( lugar == 'en_buscar_paciente'){
                cambiarContenedor('ver_resultado_busqueda', elemento);
            }

            if( lugar == 'en_formulario_estudios'){
                let get_small = document.getElementById('hint_id_paciente');

                let nombre_paciente = `
                <footer class="blockquote-footer">
                    El dni corresponde a: <cite title="Source Title" class="text-success">${paciente}</cite>
                </footer>
                `
                get_small.innerHTML = nombre_paciente;

            }

        }
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
    

}