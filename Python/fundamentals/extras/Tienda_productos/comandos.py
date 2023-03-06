
import tienda; import producto

Nintendo_swith = producto.producto('Nintendo Switch', 1650, 'Consola')
Poke_violet = producto.producto('Pokémon Violet Version', 50, 'Cartucho de juego')
Poke_scarlet = producto.producto('Pokémon Scarlet Version', 50, 'Cartucho de juego')
Cargador = producto.producto('Cargador de Nintendo Switch', 15, 'Accesorios')

Game_store = tienda.tienda('Game Store')
Game_store.agregar_producto(Poke_violet).agregar_producto(Poke_violet).agregar_producto(Poke_violet).agregar_producto(Poke_scarlet).agregar_producto(Nintendo_swith).agregar_producto(Cargador)
print(len(Game_store.productos))

Game_store.vender_producto(2)

print(Game_store.productos[0].precio)
Game_store.inflacion(7).liquidacion('Cartucho de juego', 10)
print(Game_store.productos[2].precio)

