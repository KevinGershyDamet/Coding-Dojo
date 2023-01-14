var x = 75;
if (x > 100) {    
    console.log("mayor que 100");
}
else if (x > 50) {    
    console.log(" 50");
}
else if(x > 25) {
    console.log("mayor que 25");
}
else {    
    console.log("número pequeño");
}



var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
user.push("jello");
console.log(user);
// push agrega un elemento al final del arreglo

var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
user.pop();
console.log(user);
//pop quita el último elemento del arreglo


var user = ["Dwight", "Schrute", "beetsbears@battlestar.com"];
console.log(user[0]);    // leyendo el valor -- OUTPUT: Dwight
user[1] = "Martin";    // actualizando el valor
console.log(user);
//el primer elemento del arreglo posee índice 0 ¡¡¡IMPORTANTE!!!
//si X tiene 3 elementos y se asigna un valor a X[3], se añadriá un elemento más



console.log(user.length);
//propiedad lenght indica el número de elementos del arreglo


for (var num = 0; num <= 5; num++) { //aumenta de 1 en 1
    console.log(num);
}


var arr = [2,4,6,8,10];
for (var i = 0; i < arr.length; i = i + 1) {        
    console.log(i);             // imprime el índice       
    console.log(arr[i]);        // imprime el valor del arreglo en ese índice
}

function a()
{

console.log(5);

}


a();

var variable=[[1,2],[3,1]]
variable[0][1]
//del componente 0, toma el componente 1



// los arreglos pueden escribirse como [max, min, avg]; es decir, a partir de variables creadas previamente
