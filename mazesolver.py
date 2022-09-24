import pygame, sys, random
from mazeprocess import *
from colors import colors
pygame.init()
pygame.display.set_caption('Maze solver')

size = (1000, 700)
path = 'static/maze_50x50.csv'
m, n = mazesize(path)          #tamaño mxn del maze
cell_size, x_start, y_start = displaysize(m, n)
color = random.choice(list(colors.keys()))

# #crear ventana
# screen = pygame.display.set_mode(size)
# #fps
# clock =  pygame.time.Clock()
# #cargar imagenes y escalarlas
# maze_view = pygame.image.load('static/images/maze_view.png')
# maze_view = pygame.transform.scale(maze_view, size)
# menu = pygame.image.load('static/images/menu.png')
# menu = pygame.transform.scale(menu, size)
# a = pygame.image.load('static/images/resolverpor/a.png')



# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
            
#     screen.blit(maze_view, [0, 0])
    
#     #fondo
#     mazedraw(screen, color, path, cell_size, x_start, y_start)
    
#     # screen.blit(a, [0, 0])
#     screen.blit(menu, [0, 0])
    
#     #mouse
#     mouse_pos = pygame.mouse.get_pos()
#     #zona de dibujo
    
#     #actualizar pantalla
#     pygame.display.flip()
#     clock.tick(60)
    
    
# pygame.quit()


class Game(object):
    
    def __init__(self):
        self.game_over = False


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

			# if event.type == pygame.MOUSEBUTTONDOWN:
			# 	if self.game_over:
			# 		self.__init__()

        return False

    def run_logic(self):

        if not self.game_over:
            aNN=0

    def display_frame(self, screen):

        if self.game_over:
			# font = pygame.font.SysFont("serif", 25) # Fuente
			# text = font.render("Game Over, Click To Continue", True, BLACK) # Texto
			# center_x = (SCREEN_WIDTH // 2) - (text.get_width() // 2) # posicion text
			# center_y = (SCREEN_HEIGHT // 2) - (text.get_height() // 2)
			# screen.blit(text, [center_x, center_y]) # ponerlo en pantalla
            aNN = 1

        if not self.game_over:   
            #cargar imagenes y escalarlas
            maze_view = pygame.image.load('static/images/maze_view.png')
            maze_view = pygame.transform.scale(maze_view, size)
            menu = pygame.image.load('static/images/menu.png')
            menu = pygame.transform.scale(menu, size)
            a = pygame.image.load('static/images/resolverpor/a.png')
            screen.blit(maze_view, [0, 0])
            
            #fondo
            mazedraw(screen, color, path, cell_size, x_start, y_start)
            
            # screen.blit(a, [0, 0])
            screen.blit(menu, [0, 0])

        pygame.display.flip()

def main():
    pygame.init()
    pygame.display.set_caption('Maze solver')

    #crear ventana
    screen = pygame.display.set_mode(size)
    #fps
    clock =  pygame.time.Clock()
    

    done = False
    clock = pygame.time.Clock()

    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
	main()