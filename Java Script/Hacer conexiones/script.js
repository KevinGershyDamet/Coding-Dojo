var nombres = ['Ricky Varianza', 'Willy Cotangente', 'Joe Antiderivada', 'Ana Integral'];

function aleatorio_entre (min,max) {
    output = Math.round(Math.random()*(max-min))+min;
    return output 
}

function cambiar_nombre () {
    var nombre = document.getElementById("nombre")
    var aleatorio = aleatorio_entre(0,3)
    nombre.innerText = nombres [aleatorio]
}

function eliminar_solicitud (elemento) {
    var num_sol = document.getElementById("circulo_2");
    num_sol.innerText -= 1;

    if (elemento.alt == "aceptar1" || elemento.alt == "rechazar1") {
        var por_borrar = document.querySelectorAll(".solicitud_1")
    } else {
        var por_borrar = document.querySelectorAll(".solicitud_2")
    }

    for (var i = 0 ; i < por_borrar.length ; i++) {
        por_borrar[i].remove()
    }

    if (elemento.alt == "aceptar1" || elemento.alt == "aceptar2") {
        var mas_contactos = document.getElementById("circulo_500")
        mas_contactos.innerText = parseInt(mas_contactos.innerText) + 1;
    }
}