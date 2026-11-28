from modelo.cafeteria import Cafeteria

cafe = Cafeteria(4)
print(len(cafe.mesas))             # esperado: 4
print(cafe.mesas[3].numero)        # esperado: 4
print(len(cafe._fila_puerta))              # esperado: 0
print(cafe.caja.dinero)            # esperado: 0
print(cafe.cocina is not None)     # esperado: True