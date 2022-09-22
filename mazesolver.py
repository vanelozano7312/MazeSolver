import pygame, sys
from mazeprocess import *
pygame.init()

#Colores
colors = {     
    'lilac' : (242, 193, 255),
    'purple' : (205, 127, 247),
    'violet' : (126, 52, 165)
}

size = (700, 700)
path = 'static/maze_50x50.csv'
m, n = mazesize(path)
cell_size, x_start, y_start = displaysize(m, n)

#crear ventana
screen = pygame.display.set_mode(size)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #fondo
    screen.fill(colors['purple'])
    mazedraw(screen, path, cell_size, x_start, y_start)
    
    #zona de dibujo
    
    #actualizar pantalla
    pygame.display.flip()