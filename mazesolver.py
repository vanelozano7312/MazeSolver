import pygame, sys, random
from mazeprocess import *
from colors import colors
pygame.init()

size = (700, 700)
path = 'static/maze_100x100.csv'
m, n = mazesize(path)          #tamaño mxn del maze
cell_size, x_start, y_start = displaysize(m, n)
color = random.choice(list(colors.keys()))

#crear ventana
screen = pygame.display.set_mode(size)

#fondo
screen.fill(colors[color][1])
mazedraw(screen, color, path, cell_size, x_start, y_start)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    #zona de dibujo
    
    
    #actualizar pantalla
    pygame.display.flip()