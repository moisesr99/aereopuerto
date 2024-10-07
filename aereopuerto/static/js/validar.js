

//VALIDACION PARA HOTELES
document.addEventListener("DOMContentLoaded", function() {
    let form = document.getElementById("hotel_form");

    form.addEventListener("submit", function(event) {
        // Obtener valores de los campos
        let destino = document.getElementById("HT_dest").value;
        let fechaEntrada = document.getElementById("HT_entrada").value;
        let fechaSalida = document.getElementById("HT_salida").value;
        let adultos = document.getElementById("adultos").value;

        // Convertir las fechas a objetos de tipo Date y omito la hora que genera el sistema
        let fechaEntradaObj = new Date(fechaEntrada + "T00:00:00");
        let fechaSalidaObj = new Date(fechaSalida + "T00:00:00");
        let fechaActual = new Date();
        limpiarHora(fechaActual);

        // sin manipular el horario
        //let fechaEntradaObj = new Date(fechaEntrada );
        //let fechaSalidaObj = new Date(fechaSalida );
        //let fechaActual = new Date();

        //leer la hora actual y sumarla a las fechas de entrada para volver a poner la hora actual tomandola de la fechaActual
        //no necesario para solo consulta

        // Validaciones...
        if (fechaEntradaObj >= fechaSalidaObj) {
            alert('La fecha de salida no puede ser anterior o igual a la fecha de entrada');
            event.preventDefault();
            return;
        }

        if (fechaEntradaObj < fechaActual) {
            alert('La fecha de entrada no puede ser anterior al día actual'+ fechaActual +'fecha ingresada : '+ fechaEntradaObj);
            event.preventDefault();
            return;
        }

        if (adultos <= 0) {
            alert('Debe haber al menos un adulto');
            event.preventDefault();
            return;
        }
    });

    // Función para limpiar la hora de una fecha (establecerla en 00:00:00)
    function limpiarHora(fecha) {
        if (fecha) {
            fecha.setHours(0, 0, 0, 0);  // Establece la hora en 00:00:00
        }
    }
});
//VALIDACION PARA LA PAGINA DE VUELOS
document.addEventListener("DOMContentLoaded", function() {
    let form = document.getElementById("vuelos_form");

    form.addEventListener("submit", function(event) {
        // Obtener valores de los campos
        let partida = document.getElementById("vlPart").value;
        let destino = document.getElementById("vlDest").value;
        let fechaSAL = document.getElementById("vlSalida").value;
        let fechaREG = document.getElementById("vlRegreso").value;

        // Convertir las fechas a objetos de tipo Date y forzar la hora a medianoche asi las horas tienen igualdad de condiciones
        let fechaSALObj = new Date(fechaSAL + "T00:00:00");
        let fechaREGObj = fechaREG ? new Date(fechaREG + "T00:00:00") : null;
        let fechaActual = new Date();
        limpiarHora(fechaActual);

        //let fechaSALObj = new Date(fechaSAL);
        //let fechaREGObj = fechaREG ? new Date(fechaREG) : null;
        //let fechaActual = new Date();

        // Limpiar las horas para que la comparación sea solo por fechas
        //limpiarHora(fechaSALObj);
        //if (fechaREGObj) limpiarHora(fechaREGObj);

        // Validaciones
        if (partida.length > 15 || destino.length > 15) {
            alert('El texto de búsqueda es demasiado largo');
            event.preventDefault();
            return;
        }

        if (partida === destino) {
            alert('El destino y el origen no pueden ser el mismo');
            event.preventDefault();
            return;
        }

        if (fechaSALObj < fechaActual) {
            alert('La fecha de salida no puede ser anterior al día actual. '+ fechaActual +' fecha ingresada: '+ fechaSALObj);
            event.preventDefault();
            return;
        }

        // Validar fecha de regreso si está presente
        if (fechaREGObj) {
            if (fechaSALObj >= fechaREGObj) {
                alert('La fecha de regreso no puede ser anterior o igual a la fecha de salida.');
                event.preventDefault();
                return;
            }
        }
    });

    // Función para limpiar la hora de una fecha (establecerla en 00:00:00)
    function limpiarHora(fecha) {
        if (fecha) {
            fecha.setHours(0, 0, 0, 0);  // Establece la hora en 00:00:00
        }
    }
});

