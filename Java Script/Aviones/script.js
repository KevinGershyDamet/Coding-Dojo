
// **************************************** Generación aleatoria de nubes ****************************************

nube = '<div class="nube"><div class="parte_nube_1"></div><div class="parte_nube_2"></div><div class="parte_nube_3"></div></div>'
posicion_nubes_x = []
posicion_nubes_y = []
numero_nubes = 0

function aleatorio_entre (inf, sup) { // Generación de números naturales aleatorios
    return Math.round(Math.random() * (sup - inf) + inf)
}

function posicionar_nubes () { // Posiciona nubes de manera aleatoria, grafica las nubes ya existentes

    rand = Math.random() // Determina si se añade una nube al arreglo

    if (rand < 0.1) {

        numero_nubes += 1 // Añade una nube
    
        posicion_nubes_x.push(aleatorio_entre(0,1200)) // Determina el posicionamiento aleatorio de las nubes
        posicion_nubes_y.push(-40) // Estas aparecerán en el eje horizontal superior

    }
    
    if (numero_nubes > 0) {
        
        nubes = ''
        for (var i = 1 ; i <= numero_nubes ; i++) {
            nubes += nube // Construye el arreglo con la totalidad de nubes
        }
        
        document.getElementById('campo').innerHTML = nubes
    
        for (var i = 0 ; i < document.querySelectorAll('.nube').length ; i++) { // Asigna el posicionamiento a cada nube
            document.querySelectorAll('.nube')[i].style.top = posicion_nubes_y[i] + 'px'
            document.querySelectorAll('.nube')[i].style.left = posicion_nubes_x[i] + 'px'
        }
    }
        

}

function desplazar_nubes () { // Genera el desplazamiento de nubes

    nubes_volando = document.querySelectorAll('.nube') // Las nubes se desplazarán verticalmente a un ritmo de 10px por u.t.
    for (var i = 0 ; i < nubes_volando.length ; i++) {
        posicion_nubes_y[i] += 10
        nubes_volando[i].style.top = posicion_nubes_y[i] + 'px' 
    }

    if (posicion_nubes_y[0] >= 700) {
        numero_nubes += -1
        posicion_nubes_x.shift()
        posicion_nubes_y.shift()
    }

    posicionar_nubes()

}

setInterval(function () {desplazar_nubes()}, 50)




// **************************************** Desplazamiento del jugador ****************************************




// Creación del jugador en posición inicial
codigo_jugador = '<div class="cuerpo jugador"></div><div class="cola jugador"></div><div class="ala jugador"></div>'
jugador = document.getElementById('jugador')
jugador.innerHTML = codigo_jugador

// Posición del jugador
pos_jugador = {x: 600, y: 500} 

// Grafica al jugador en la posición actual
function grafica_jugador() { 
    jugador.style.top = pos_jugador.y + 'px'; jugador.style.left = pos_jugador.x + 'px'
}
grafica_jugador()

// Desplazamiento del jugador (condicionada a ubicarse dentro del campo)
document.onkeydown = function(e) {
    if (e.key == 'ArrowLeft' && pos_jugador.x >= 20) {
        pos_jugador.x += -10
    } else if (e.key == 'ArrowRight' && pos_jugador.x <= 1100) {
        pos_jugador.x += 10
    } else if (e.key == 'ArrowDown' && pos_jugador.y <= 600) {
        pos_jugador.y += 10
    } else if (e.key == 'ArrowUp' && pos_jugador.y >= 300) {
        pos_jugador.y += -10
    }

    //Además, detecta el lanzamiento de misiles
    if (e.key == ' ') {
        tiros.x.push(pos_jugador.x + 45); tiros.y.push(pos_jugador.y - 10) 
        num_misiles += 1
        grafica_misiles()
    }

    grafica_jugador()
}




// **************************************** Mecánicas de misiles ****************************************




misil = '<div class=misil></div>'
num_misiles = 0
tiros = {x: [] , y: []}

// Gráfica de misiles
function grafica_misiles() {
    if (num_misiles > 0) {
        
        misiles = ''
        for (var i = 1 ; i <= num_misiles ; i++) {
            misiles += misil
        }

        document.getElementById('misiles').innerHTML = misiles

        misiles_lanzados = document.querySelectorAll('.misil')
        
        for (var j = 0 ; j < misiles_lanzados.length ; j++) {
            misiles_lanzados[j].style.left = tiros.x[j] + 'px'; misiles_lanzados[j].style.top = tiros.y[j] + 'px'
        }

    }
}

// Desplazamiento de misiles
function desplaza_misiles() {
    if (num_misiles > 0) {

        for (var i = 0 ; i < num_misiles ; i++) {
            tiros.y[i] += -5;
        }

        grafica_misiles()

    }
}

setInterval (function () {desplaza_misiles()}, 10)


