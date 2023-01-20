function getSecondsSinceStartOfDay() {
    var tiempo = [new Date().getSeconds() , new Date().getMinutes() , new Date().getHours()];
    
    segundos = document.getElementById('seconds')
    minutos = document.getElementById('minutes')
    hora = document.getElementById('hour')

    segundos.style.transform = 'rotate(' + (180 + tiempo[0] / 60 * 360) + 'deg)'
    minutos.style.transform = 'rotate(' + (180 + tiempo[1] / 60 * 360 + tiempo[0] / 3600 * 360) + 'deg)'
    hora.style.transform = 'rotate(' + (180 + tiempo[2] / 12 * 360 + tiempo[1] / 60 / 12 * 360 + tiempo[0] / 3600 / 12 * 360) + 'deg)'
}
getSecondsSinceStartOfDay()
setInterval(getSecondsSinceStartOfDay, 1000);
