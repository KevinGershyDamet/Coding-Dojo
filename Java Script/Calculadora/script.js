
var operacion = "";
var desactivar = "";

function setOP (ope) {
    mostrador = document.getElementById('display')
    operacion += mostrador.innerText;
    operacion += ope
    desactivar = "si";
}

function press(valor) {
    mostrador = document.getElementById('display')

    if (mostrador.innerText == 0 || desactivar == "si") {
        if (valor == ".") {
            mostrador.innerText += valor;
        } else {
            mostrador.innerText = valor;    
        }
        desactivar = "";
    } else {
        mostrador.innerText += valor;
    }
}

function clr() {
    mostrador = document.getElementById('display')
    mostrador.innerText = 0;
    operacion = "";
}

function calculate() {
    mostrador = document.getElementById('display')
    operacion += mostrador.innerText;
    individuales = operacion.split('');

        var operadores = [];
        var numeros = [];
        var numero = [];
        for (var i = 0 ; i < individuales.length ; i++) {
            if (isNaN(parseInt(individuales[i])) && individuales[i] != "." ) {
                operadores.push(individuales[i])
                numeros.push(parseFloat(numero.join('')))
                numero = []
            } else if (isNaN(parseInt(individuales[i])) == false && i == individuales.length - 1) {
                numero.push(individuales[i])
                numeros.push(parseFloat(numero.join('')))
            } else {
                numero.push(individuales[i])
            }
        }

        var resultado = numeros[0];
        for (var j = 0 ; j < operadores.length ; j++) {
            if (operadores[j] == "*") {
                resultado = resultado * numeros[j+1]
            } else if (operadores[j] == "+") {
                resultado = resultado + numeros[j+1]
            } else if (operadores[j] == "/") {
                resultado = resultado / numeros[j+1]
            } else {
                resultado = resultado - numeros[j+1]
            }
        }

        
    mostrador.innerText = resultado;
    operacion = "";
    desactivar ="si";
}