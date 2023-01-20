function pizzaOven (corteza, salsas, quesos, proteina) {
    var pizza = {};
    pizza.corteza = corteza;
    pizza.salsas = salsas;
    pizza.quesos = quesos;
    pizza.proteina = proteina;
    return pizza
}

var pizza1 = pizzaOven("estilo chicago", "tradicional", ["mozzarella"], ["pepperoni", "salchicha"])
console.log(pizza1);

var pizza2 = pizzaOven("lanzada a mano", "marinara", ["mozzarella", "feta"], ["champiñones", "aceitunas","cebollas"])
console.log(pizza2)

var pizza3= pizzaOven("hojaldre", "tomate", "mozzarella", "pepperoni")
var pizza4 = pizzaOven("gruesa", "tomate", "gouda", ["piña", "jamón"])