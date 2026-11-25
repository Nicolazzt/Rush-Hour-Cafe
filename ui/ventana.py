import pygame
from ui.dibujo import dibujar_mesa
from modelo.mesa import Mesa 
from modelo.cliente import ClienteTranquilo
pygame.init()

pantalla = pygame.display.set_mode((920,480))
clock = pygame.time.Clock()
run = True
mesa1 = Mesa(1)
mesa2 = Mesa(2)
mesa3 = Mesa(3)
mesa4 = Mesa(4)
cliente1 = ClienteTranquilo()

mesa2.sentar(cliente1)
mesa3.ensuciar()
mesas = [mesa1,mesa2,mesa3,mesa4]

while run:
    #pygame.QUIT significa que el usuario cerrara la ventana cuando cliquee X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)

    #fill pinta toda la ventana de un color. Es una tupla de 3 numeros
    pantalla.fill((235, 245, 252))

    for i, Mesa in enumerate(mesas): #bucle para llamar 1 sola vez a dibujar mesa y que se dibujen no importa cuantas hallan dentro de la lista
        x = (i + 1) * 100
        dibujar_mesa(pantalla,Mesa,x,200)
        

    #flip muestra en pantalla lo que se dibuja
    pygame.display.flip()


pygame.quit()