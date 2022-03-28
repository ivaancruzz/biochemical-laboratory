ESTUDIOS = [
    'General', 'Hemograma', 'Embarazada', 'Hepatograma','Orina','Urocultivo',
    'Proteinograma', 'Quimica', 'Cultivo', 'Parasitologico',
]

function crearOpciones(){
    select = document.getElementById('estudios');

    for( let i = 0; i<ESTUDIOS.length;i++){
        let new_option = document.createElement('option')
        new_option.setAttribute( 'value', i )

        if( i == 0 ){
            new_option.setAttribute( 'selected', 'selected' )
        }

        let add_text = document.createTextNode( ESTUDIOS[i] )

        new_option.appendChild( add_text )
        select.appendChild( new_option )

    }
}
let anterior = ''

function cambiarFormulario(){
    select = document.getElementById('estudios').value;

    for( let i = 0; i<ESTUDIOS.length;i++){
        if( i == select ){
            document.getElementById( i ).setAttribute( 'style', 'display: block' );
        } else{
            document.getElementById( i ).setAttribute( 'style', 'display: none' );
        }
        
    } 
}
crearOpciones()