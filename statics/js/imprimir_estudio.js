function imprimir( fecha_estudio, nombre_paciente, nombre_estudio, resultadosJS, observaciones ){
    let nombre_analisis = obtenerAnalisisPorSeparado( resultadosJS )[0];
    let resultado_analisis = obtenerAnalisisPorSeparado( resultadosJS )[1];
    let valores_referencia = obtenerAnalisisPorSeparado( resultadosJS )[2];

    crearPDF( fecha_estudio, nombre_paciente, nombre_estudio, nombre_analisis, resultado_analisis, valores_referencia, observaciones);
    
}

function crearPDF( fecha_estudio, nombre_paciente, nombre_estudio, n_analisis, r_analisis, val_ref, observacion ){
    const pdf = new jsPDF();

    //Datos dinamicos
    const titulo = 'Laboratorio de análisis clínicos Mariano Moreno'
    const nombre = 'Paciente: ' + nombre_paciente
    const fecha = 'El estudio se realizo el: ' + fecha_estudio
    const tipo_estudio = 'Estudio realizado: ' + nombre_estudio
    const observaciones = observacion.replace(/[´]/g, '\n')
    const al_dr = 'Al dr: '
    const atte = 'Atte: '
    const dire = 'Alvear 762 - Jujuy';


    //PDF diseño cabecera

    //Titulo
    pdf.setFont('helvetica', 'bold');
    pdf.setTextColor( 69, 130, 236 ) //Celeste
    pdf.setFontSize( 18 );
    pdf.text(titulo, 30, 10)

    //Textos abajo del titulo
    pdf.setFont('helvetica', 'normal');
    pdf.setTextColor( 0, 0, 0 ) //negro
    pdf.setFontSize( 9 );

    pdf.text(nombre, 10, 20)
    pdf.text(fecha, 10, 25)

    pdf.text(al_dr, 100, 20)
    pdf.text(atte, 100, 25)
    pdf.text(dire, 170, 30)

    //Linea
    pdf.setLineWidth(0.5);
    pdf.line( 10, 35, 200, 35 )



    //Tabla
    if( nombre_estudio != 'General' ){
        //Seccion observacion
        pdf.setFont('helvetica', 'bold');
        pdf.setTextColor( 69, 130, 236 ) //Celeste
        pdf.setFontSize( 12 );
        pdf.text('Observaciones:', 10, 265 )

        pdf.setTextColor( 0, 0, 0 ) //negro
        pdf.setFontSize( 8.5 );
        pdf.setFont('helvetica', 'normal');
        pdf.text( observaciones, 10, 270 )

        //Resultados
        pdf.setFont('helvetica', 'bold');
        pdf.setTextColor( 69, 130, 236 ) //Celeste
        pdf.setFontSize( 12 );
        pdf.text('Resultados:', 10, 40 )

        pdf.setTextColor( 0, 0, 0 ) //negro
        pdf.setFontSize( 9 );
        pdf.setFont('helvetica', 'normal');
        pdf.text(tipo_estudio, 10, 30)

        //PDF estructura tabla
        const header_tabla = [
            ['Tipo', 'Resultado', 'Valor de referencia']
        ]

        let cuerpo_tabla = []

        for( i = 0; i < n_analisis.length ;i++){
            cuerpo_tabla.push( [ n_analisis[i], r_analisis[i], val_ref[i] ] );
        }

        //PDF diseño tabla
        pdf.setTextColor( 2, 184, 117 ) //Verde agua
        pdf.setFontSize( 16 );

        pdf.autoTable({
            theme: 'plain',
            headStyles: { halign: 'left' },
            bodyStyles: { halign: 'left' },
            margin: { top: 45},
            head: header_tabla,
            body: cuerpo_tabla
        });

    } else {


        cuerpo_tabla = []
        for( i = 0; i < n_analisis.length ;i++){
            cuerpo_tabla.push(  r_analisis[i]  );
        }

        //Titulo analisis solicitado
        pdf.setFont('helvetica', 'bold');
        pdf.setTextColor( 69, 130, 236 ) //Celeste
        pdf.setFontSize( 10 );
        pdf.text('Analisis solicito:', 10, 40 )

        //Muestra del analisis
        pdf.setFont('helvetica', 'normal');
        pdf.setTextColor( 0, 0, 0 ) //Celeste
        pdf.setFontSize( 9 );
        pdf.text(cuerpo_tabla[0], 40, 40)

        //Titulo detalles
        pdf.setFont('helvetica', 'bold');
        pdf.setTextColor( 69, 130, 236 ) //Celeste
        pdf.setFontSize( 10 );
        pdf.text('Detalles:', 10, 50 )

        //Detalles
        let detalle = cuerpo_tabla[1].replace(/[´]/g, '\n\n')

        pdf.setFont('helvetica', 'normal');
        pdf.setTextColor( 0, 0, 0 ) //Celeste
        pdf.setFontSize( 9 );
        pdf.text(detalle, 10, 55)


    }


    window.open(pdf.output('bloburl'))
    
}

// **** Obtenemos un STRING completo con todo los valores del estudio
// En esta funcion separamos todo asi podemos manipularlo mejor
function obtenerAnalisisPorSeparado( cb ){
    let resultados_del_estudio = dividirCadena( cb, '**');
    let nombre_analisis = []
    let resultado_analisis = []
    let valores_referencia = []

    resultados_del_estudio.forEach(element => {
        const NOMBRE_ANALISIS = 0;
        const RESULTADO_ANALISIS = 1;
        const VALORES_REFERENCIA = 2;

        let obtener_elemento = dividirCadena( element, '_' );
        nombre_analisis.push( obtener_elemento[NOMBRE_ANALISIS] )
        resultado_analisis.push( obtener_elemento[RESULTADO_ANALISIS] )
        valores_referencia.push( obtener_elemento[VALORES_REFERENCIA] )

    });

    return [ nombre_analisis, resultado_analisis, valores_referencia ]
}

// Divide la cadena por un separador
function dividirCadena( cadena_a_dividir, separador ){
    let array_de_cadenas = cadena_a_dividir.split( separador ); //Dividimos la cadena por el separador y lo guardamos

    return array_de_cadenas;
}

function reemplazarCadena( cadena_a_dividir, cadena_a_reemplazar, cadena_actual ){
    let regex = /cadena_a_reemplazar/g
    let cadena_nueva = cadena_a_dividir.replace(/cadena_a_reemplazar /g, cadena_actual)

    return cadena_nueva;
}

