function deshabilitaRetroceso(){
    window.location.hash="no-back-button";
    window.location.hash="Again-No-back-button" //chrome
    window.onhashchange=function(){window.location.hash="Again-No-back-button";} //agregar entre las comillas Again-No-back-button, en caso que no funciones
}
window.onpageshow = function(event) {
    if (event.persisted) {
        window.location.reload();  // Recargar la página al regresar
    }
};
window.onload = function() {
    document.forms[0].reset();  // Restablece el primer formulario en la página
};
// Obtener el checkbox y deshabilitar el input de fecha de regreso
const switchCheck = document.getElementById('flexSwitchCheckDefault');
const returnInput = document.getElementById('vlRegreso');
returnInput.disabled = true; //pondra el input de regreso por default

// Agregar un evento que escuche cuando se cambie el estado del checkbox
switchCheck.addEventListener('change', function() {
    if (this.checked) {
        // Si el checkbox está activado, deshabilitar el campo de regreso
        returnInput.disabled = false;
    } else {
        // Si el checkbox está desactivado, habilitar el campo de regreso
        returnInput.disabled = true;
    }
});
// cambiar color de botones para viaje sencillo y redondo
document.getElementById('flexSwitchCheckDefault').addEventListener('change', function() {
    var sencilloLabel = document.getElementById('sencilloLabel');
    var redondoLabel = document.getElementById('redondoLabel');

    if (this.checked) {
        sencilloLabel.classList.remove('activo');
        sencilloLabel.classList.add('inactivo');

        redondoLabel.classList.remove('inactivo');
        redondoLabel.classList.add('activo');
        
    } else {
        sencilloLabel.classList.remove('inactivo');
        sencilloLabel.classList.add('activo');

        redondoLabel.classList.remove('activo');
        redondoLabel.classList.add('inactivo');
        
    }
});



