function siempre_hambriento (arreglo) {
    var cont = 0;
    for (var i =0 ; i < arreglo.length ; i++) {
        if (arreglo[i] == "comida") {
            console.log("delicioso")
            cont++
        } 
    }   
    if (cont == 0) {
        console.log('tengo hambre')
    }
}

var arr1 = [1, 2, 'comida', 'comida', 3, 'comida', 'comida']
var arr2 = [1, 2, 3, 4, 5, 6, 7]

siempre_hambriento(arr1)
siempre_hambriento(arr2)

function por_encima (arreglo , corte) {
    var resultado = [];
    for (var i = 0 ; i < arreglo.length ; i++) {
        if (arreglo[i] > corte) {
            resultado.push(arreglo[i])
        }
    }
    console.log(resultado)
    return resultado
}

var corte = 2;
por_encima(arr2, corte)


function mejor_que_promedio (arreglo) {
    var promedio = 0;
    for (var i = 0 ; i < arreglo.length ; i++) {
        promedio += arreglo[i] / arreglo.length
    }
    var count = 0;
    for (var i = 0 ; i < arreglo.length ; i++) {
        if (arreglo[i] > promedio) {
            count++
        }
    }
    console.log(count)
    return count
}

mejor_que_promedio(arr2)

function reverso (arreglo) {
    var nuevo = [];
    for (var i = 0 ; i < arreglo.length ; i++) {
        nuevo.push(arreglo[arreglo.length - 1 - i])
    }
    return nuevo
}

console.log(reverso(arr2))

function sucFibo (n) {
    var arrFibo = [];
    for (var i = 0 ; i < n ; i++) {
        if (i < 2) {
            arrFibo.push(i)
        } else {
            arrFibo.push(arrFibo[i-1]+arrFibo[i-2])
        }
    }
    return arrFibo;
}

console.log(sucFibo(10))