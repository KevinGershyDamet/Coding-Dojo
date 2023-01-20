for (var i = 1 ; i <= 20 ; i++) {
    if (i%2 != 0) {
        console.log(i)
    }
}

for (var i = 100 ; i >= 0 ; i--) {
    if (i%3 == 0) {
        console.log(i)
    }
}

for (var i = 4 ; i >= -3.5 ; i -= 1.5) {
    console.log(i)
}

var sum = 1;
var texto = "1";
for (var i = 2 ; i <= 100 ; i++) {
    sum += i
    texto += "+" + i
}
console.log(sum)
console.log(texto)

var product = 1;
var texto = "1";
for (var i = 2 ; i <= 12 ; i++) {
    product *= i
    texto += "*" + i
}
console.log(product)
console.log(texto)