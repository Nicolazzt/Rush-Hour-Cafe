from modelo.enums import EstadoMesa
import pygame

COLORES_ESTADOS_MESA = {
    EstadoMesa.LIBRE : (222,200,165),
    EstadoMesa.OCUPADA : (245,200,66),
    EstadoMesa.SUCIA : (139,90,43)
}

def dibujar_mesa(superficie, mesa, x, y):
    pygame.draw.rect(superficie,COLORES_ESTADOS_MESA[mesa.estado],(x, y, 60, 60) )
