var grados_celsius = [24, 18, 27, 19, 21, 16, 26, 21];
var grados_farenheit = [];
var grados_kelvin = [];
    for (var j = 0 ; j < 8 ; j++) {
        grados_farenheit.push(grados_celsius[j] * 9/5 + 32)
        grados_kelvin.push(grados_celsius[j] + 273.15)
    }

function hide () {
    var mensaje = document.getElementById("aviso_cookie");
    mensaje.remove();
}

function convertir (elemento) {
    var grados = document.querySelectorAll(".temp");

    if (elemento.value == "°C") {
        var cambio = grados_celsius;
    } else if (elemento.value == "°F") {
        var cambio = grados_farenheit;
    } else {
        var cambio = grados_kelvin;
    }

    for (var i = 0 ; i <= 7 ; i++) {
        grados[i].innerText = cambio[i] + "°"
    }
}

