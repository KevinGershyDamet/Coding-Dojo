function sesion (elemento) {
    if (elemento.innerText == 'LogIn') {
        elemento.innerText = 'LogOut'
    } else {
        elemento.innerText = 'LogIn'
    }
}

function cambio_version (elemento) { // Nótese que múltiples secciones de la página aluden a la versión vigente
    var cambios = document.querySelectorAll('.version_actual')
        
    for (var i = 0 ; i < cambios.length ; i++) {
        var num_caracteres = cambios[i].innerText.length
        
        if (num_caracteres == 5) { // En la segunda ocurrencia, el carecter "v" se encuentra separado
            cambios[i].innerText = elemento.value.replace(/v/,'') + '.1'
        } else {
            cambios[i].innerText = elemento.value + '.1'
        }
    }
}