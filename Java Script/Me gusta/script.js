var valores = [9, 12, 9];

function actualizar_likes (boton) {
    
    var numero_likes = document.querySelectorAll(".num_likes");
    
    for (var i=1 ; i<=3 ; i+=1) {
        if (boton.id == "boton_"+i) {
            valores[i-1] += 1;
            numero_likes[i-1].innerText = valores[i-1] + " like(s)"; 
        }
    }
}


