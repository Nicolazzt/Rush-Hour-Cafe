from modelo.cliente import ClienteTranquilo

t = ClienteTranquilo()
t.avanzar(5);    t.siguiente_fase()
t.avanzar(4.8);  t.siguiente_fase()
t.avanzar(22.5); t.siguiente_fase()
t.avanzar(15)
t.avanzar(6);    t.siguiente_fase()
print(t.satisfaccion())    # esperado: 65, o muy cerca