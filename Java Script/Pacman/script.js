
// ******************************************* Mecánicas para Pacman ******************************************* //




direc = ''; // Especifica la dirección inicial

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
}

var pos_pacman = { // Coordenada de Pacman
    x: 1,
    y: 1,
}

function graf_pacman () { // Grafica a Pacman en su ubicación actual
    document.querySelector('.pacman').style.left = (pos_pacman.x * 50 + 8) + 'px'
    document.querySelector('.pacman').style.top = (pos_pacman.y * 50 + 9) + 'px'
}

function desplazar (direc) { // Actualiza la posición actual de Pacman

    if (direc == 'comida_right' && mazmorra[pos_pacman.y][pos_pacman.x + 1] != 1) {
        pos_pacman.x += 1;
    } else if (direc == 'comida_left' && mazmorra[pos_pacman.y][pos_pacman.x - 1] != 1) {
        pos_pacman.x += -1
    } else if (direc == 'comida_up' && mazmorra[pos_pacman.y - 1][pos_pacman.x] != 1) {
        pos_pacman.y += -1
    } else if (direc == 'comida_down' && mazmorra[pos_pacman.y + 1][pos_pacman.x] != 1) {
        pos_pacman.y += 1
    }
    graf_pacman()
    eliminar_comida(pos_pacman.x, pos_pacman.y)
    tocar_fantasma()
    
}




// ******************************************* Creación de la mazmorra para Pacman ******************************************* //




var elementos_mundo = { // Tipos de elementos que tendrá la mazmorra
    0: '<div class="vacio mazmorra"></div>', // Vacío
    1: '<div class="pared mazmorra"><div class="luz"></div></div>', // Pared
    2: '<div class="comida_normal mazmorra"><div class="limon"></div></div>', // Limón
    3: '<div class="cereza mazmorra"><div class="tallo_1"></div><div class="tallo_2"></div><div class="gajo_1"></div><div class="gajo_2"></div></div>', // Cereza
}

var mazmorra = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

codigo_mazmorra = ""; // Creación de las divisiones HTML que representarán a la mazmorra
for (var i = 0 ; i < mazmorra.length ; i++) {
    codigo_mazmorra += '<div class="row">'
    
    for (var j = 0 ; j < mazmorra[i].length ; j++) {
        
        if (mazmorra[i][j] == 0) {
            comida_aleatoria = Math.random()
            if (comida_aleatoria < 0.05) { // Las cerezas se colocarán en porcentaje menor
                mazmorra[i][j] = 3
            } else {
                mazmorra[i][j] = 2
            }
        }

        codigo_mazmorra += elementos_mundo[mazmorra[i][j]]

    }

    codigo_mazmorra += '</div>'
}
document.getElementById('mundo').innerHTML = codigo_mazmorra;

cuadros_por_cambiar = document.querySelectorAll('.mazmorra')
function eliminar_comida (a, b) { // Permite eliminar la comida conforme Pacman se desplace

    if (cuadros_por_cambiar[(b * mazmorra[0].length) +   a].classList == 'comida_normal mazmorra') {

        puntaje += 5
        cuadros_por_cambiar[(b * mazmorra[0].length) +   a].classList.remove('comida_normal')

    } else if (cuadros_por_cambiar[(b * mazmorra[0].length) +   a].classList == 'cereza mazmorra') {

        puntaje += 50
        cuadros_por_cambiar[(b * mazmorra[0].length) +   a].classList.remove('cereza')

    } // La remoción de la clase ('cereza' o 'comida_normal') permite que ya no se acumule puntaje en la siguiente ocasión en la que pacman pase por dicha casilla
    
    cuadros_por_cambiar[(b * mazmorra[0].length) +   a].innerHTML = elementos_mundo['0']

    // Esta acción además permite actualizar el puntaje según la comida eliminada
    estado = '<span>Jugador: Kev<br>Vidas: ' + vidas + '<br>Puntaje: ' + puntaje + ' ptos</span>' 
    document.querySelector('.texto_puntaje').innerHTML = estado

}

function luces_intermitentes () { // Recrea el cambio de color de las luces
    
    luces = document.querySelectorAll('.luz')
    color = seleccion_aleatoria(['red', 'yellow', 'white', 'blue', 'purple'])
    
    for (var i = 0 ; i < luces.length ; i++) {
        luces[i].style.backgroundColor = color
    }
    
}




// ******************************************* Mecánicas para fantasmas ******************************************* //




function aleatorio_entre (inf, sup) { // Generación de números naturales aleatorios
    return Math.round(Math.random() * (sup - inf) + inf)
}

function seleccion_aleatoria (arreglo) { // Selecciona un elemento aleatorio de un arreglo cualquiera
    indice = aleatorio_entre(0, arreglo.length - 1)
    return arreglo[indice]
}

num_fantasmas = aleatorio_entre(1,3) // Generación de cantidad aleatoria de fantasmas (con posiciones iniciales respectivas)
fantasmas_graficados = ""
pos_aleat_x = []; pos_aleat_y = [];
for (var i = 1 ; i <= num_fantasmas ; i++) {
    fantasmas_graficados += '<div class="fantasma"><div class="ojo"><div class="pupila"></div></div><div class="ojo"><div class="pupila"></div></div></div>'
    pos_aleat_x.push(aleatorio_entre(14, mazmorra[0].length - 1))
    pos_aleat_y.push(aleatorio_entre(9, mazmorra.length - 1))
}
document.getElementById('oponentes').innerHTML = fantasmas_graficados


var pos_fantasma = { // Definición de la posición inicial (aleatoria) para cada fantasma
    x: pos_aleat_x,
    y: pos_aleat_y,
}

function graf_fantasma () { // Grafica a los fantasmas en su posición actual
    fant = document.querySelectorAll('.fantasma')

    for (var i = 0 ; i < fant.length ; i++) {
        fant[i].style.left = (pos_fantasma.x[i] * 50 + 8) + 'px'
        fant[i].style.top = (pos_fantasma.y[i] * 50 + 9) + 'px'    
    }
}

function desplazar_fantasmas () { // Desplaza a los fantasmas hacia direcciones aleatorias (uno por uno)
    fant = document.querySelectorAll('.fantasma')
    ojos = document.querySelectorAll('.ojo')

    for (var i = 0 ; i < fant.length ; i++) {
        
        // Determina la acción aleatoria condicionada a perseguir a pacman
        if (pos_pacman.x > pos_fantasma.x[i]) { // Si pacman se encuentra a la derecha
            desplazamiento_horizontal = 1 
        } else {
            desplazamiento_horizontal = 2
        }
        if (pos_pacman.y > pos_fantasma.y[i]) { // Si pacman se encuentra por debajo
            desplazamiento_vertical = 3
        } else {
            desplazamiento_vertical = 4
        }
        accion = seleccion_aleatoria([desplazamiento_horizontal, desplazamiento_vertical])

        // Realización de acciones
        if (accion == 1 && mazmorra[pos_fantasma.y[i]][pos_fantasma.x[i] + 1] != 1) { // Desplazamiento hacia la derecha
            
            pos_fantasma.x[i] += 1
            
            for (var oj = 0 ; oj <= 1 ; oj++) {
                ojos[i * 2 + oj].style.justifyContent = 'end'
                ojos[i * 2 + oj].style.alignItems = 'center'
            }

        } else if (accion == 2 && mazmorra[pos_fantasma.y[i]][pos_fantasma.x[i] - 1] != 1) { // Desplazamiento hacia la izquierda
            
            pos_fantasma.x[i] += -1
            
            for (var oj = 0 ; oj <= 1 ; oj++) {
                ojos[i * 2 + oj].style.justifyContent = 'start'
                ojos[i * 2 + oj].style.alignItems = 'center'
            }

        } else if (accion == 3 && mazmorra[pos_fantasma.y[i] + 1][pos_fantasma.x[i]] != 1) { // Desplazamiento hacia abajo
            
            pos_fantasma.y[i] += 1

            for (var oj = 0 ; oj <= 1 ; oj++) {
                ojos[i * 2 + oj].style.justifyContent = 'center'
                ojos[i * 2 + oj].style.alignItems = 'end'
            }

        } else if (accion == 4 && mazmorra[pos_fantasma.y[i] - 1][pos_fantasma.x[i]] != 1) { // Desplazamiento hacia arriba
            
            pos_fantasma.y[i] += -1

            for (var oj = 0 ; oj <= 1 ; oj++) {
                ojos[i * 2 + oj].style.justifyContent = 'center'
                ojos[i * 2 + oj].style.alignItems = 'start'
            }

        }
    }

    graf_fantasma()
}

graf_fantasma()

function tocar_fantasma () { // Reinicia la posición de Pacman una vez que a este lo atrapa un fantasma

    contador_fantasmas = 0

    for (var i = 0 ; i < pos_aleat_x.length ; i++) {

        // Este condicional permite que el fantasma atrape a Pacman si ambos se mueven hacia casillas adyacentes
        if ((pos_pacman.x == pos_aleat_x[i] && Math.abs(pos_pacman.y - pos_aleat_y[i]) <= 1) || (pos_pacman.y == pos_aleat_y[i] && Math.abs(pos_pacman.x - pos_aleat_x[i]) <= 1)) {
            
            contador_fantasmas += 1

        }

    }

    if (contador_fantasmas > 0) {
        pos_pacman.x = 1; pos_pacman.y = 1;
        direc = '' // Además, reinicia la dirección a la cual apunta Pacman
        vidas += -1 // Asimismo, reduce un intento al jugador

        for (var i = 0 ; i < pos_aleat_x.length ; i++) { // Finalmente, vuelve a colocar a los fantasmas en posiciones aleatorias
        pos_aleat_x[i] = (aleatorio_entre(14, mazmorra[0].length - 1))
        pos_aleat_y[i] = (aleatorio_entre(9, mazmorra.length - 1))
        }
    }

    if (vidas == 0) {
        // Esta sección actualiza la tabla de puntaje con la nueva cantidad de intentos
        estado = '<span>Jugador: Kev<br>Vidas: ' + vidas + '<br>Puntaje: ' + puntaje + ' ptos</span>' 
        document.querySelector('.texto_puntaje').innerHTML = estado

        alert('GAME OVER') // Alerta de fin de juego

        // Finalmente, cierra la ventana
        window.close()
    }

}




// ******************************************* Funcionamiento del puntaje ******************************************* //




codigo_puntaje = "" // Creación del tablero de puntaje
for (var i = 1 ; i <= 7 ; i++) {

    codigo_puntaje += '<div class="row">'

    for (var j = 1 ; j <= 12 ; j++) {

        if (j > 1 && j < 12 && i > 1 && i < 7) {
            codigo_puntaje += '<div class="vacio_puntaje"></div>'
        } else {
            codigo_puntaje += '<div class="adorno_puntaje"></div>'
        }
        
    }

    codigo_puntaje += '</div>'

}
codigo_puntaje += '<p class="texto_puntaje"></p>' 
document.getElementById('puntaje').innerHTML = codigo_puntaje

puntaje = 0; vidas = 5; // Agrgación del texto sobre el estado del jugador
estado = '<span>Jugador: Kev<br>Vidas: ' + vidas + '<br>Puntaje: ' + puntaje + ' ptos</span>' 
document.querySelector('.texto_puntaje').innerHTML = estado




// ******************************************* Correr el juego ******************************************* //




setInterval(function () {comer(direc)}, 100) // Es necesario crear una función anónima primero
setInterval(function () {desplazar(direc)}, 100)
setInterval(function () {desplazar_fantasmas()}, 100)
setInterval(function () {luces_intermitentes()}, 700)




