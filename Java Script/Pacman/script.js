
// ************************ Mecánicas para Pacman ************************ //




direc = 'comida_right';

document.onkeydown = function(e) { // Permite modificar la instrucción de dirección
    if (e.key == 'ArrowLeft') {
        direc = 'comida_left'
    } else if (e.key == 'ArrowRight') {
        direc = 'comida_right'
    } else if (e.key == 'ArrowUp') {
        direc = 'comida_up'
    } else if (e.key == 'ArrowDown') {
        direc = 'comida_down'
    }
}

function comer (direc) { // Permite que Pacman apunte hacia la dirección deseada
    jugador =  document.querySelector('.pacman');
    if (jugador.classList == 'pacman') {
        jugador.classList.add(direc);
    } else {
        jugador.classList = 'pacman';
    }
    console.log(jugador.classList)
}

var pos_pac = { // Coordenada de Pacman
    x: 10,
    y: 10,
}

function graf_pacman () { // Grafica a Pacman en su ubicación actual
    document.querySelector('.pacman').style.left = pos_pac.x + 'px'
    document.querySelector('.pacman').style.top = pos_pac.y + 'px'
}

function desplazar (direc) { // Actualiza la posición actual de Pacman
    if (direc == 'comida_right') {
        pos_pac.x += 50;
    } else if (direc == 'comida_left') {
        pos_pac.x += -50
    } else if (direc == 'comida_up') {
        pos_pac.y += -50
    } else {
        pos_pac.y += 50
    }
    graf_pacman()
}

setInterval(function () {comer(direc)}, 100) // Es necesario crear una función anónima primero
setInterval(function () {desplazar(direc)}, 300)




// ************************ Creación de la mazmorra para Pacman ************************ //




var elementos_mundo = { // Tipos de elementos que tendrá la mazmorra
    0: 'vacio',
    1: 'pared',
    2: 'simple',
    3: 'cereza',
}

var mazmorra = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

codigo_mazmorra = ""; // Creación de las divisiones HTML que representarán a la mazmorra
for (var i = 0 ; i < mazmorra.length ; i++) {
    codigo_mazmorra += '<div class="row">'
    
    for (var j = 0 ; j < mazmorra[i].length ; j++) {
        codigo_mazmorra += '<div class="' + elementos_mundo[mazmorra[i][j]] + '"></div>'
    }

    codigo_mazmorra += '</div>'
}
document.getElementById('mundo').innerHTML = codigo_mazmorra;