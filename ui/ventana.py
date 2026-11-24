import pygame
from ui.dibujo import dibujar_mesa
from modelo.mesa import mesa 
pygame.init()

pantalla = pygame.display.set_mode((920,480))
clock = pygame.time.Clock()
run = True
mesa1 = mesa(1)
mesa2 = mesa(2)
mesa3 = mesa(3)


while run:
    #pygame.QUIT significa que el usuario cerrara la ventana cuando cliquee X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)

    #fill pinta toda la ventana de un color. Es una tupla de 3 numeros
    pantalla.fill((245, 230, 240))

    dibujar_mesa(pantalla,mesa1,300,200)

    #flip muestra en pantalla lo que se dibuja
    pygame.display.flip()


pygame.quit()