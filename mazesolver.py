import pygame, sys, random
from mazeprocess import *
from colors import colors

size = (1000, 700)


class Game(object):
    
    def __init__(self):
        self.solved_maze = False
        self.page = 'home'              #posibles páginas: home, maze
        self.solve_method =''           #posibles methods: a:anchura, ae:a*, bdcu:búsqeda de costo uniforme, bg:búsqueda greedy
                                        #p: profundidad, pi:profundidad iterativa, '': no se ha escogido
        self.path = 'static/mazes/maze_50x50.csv'
        self.m, self.n = maze_size(self.path)          #tamaño mxn del maze
        self.cell_size, self.x_start, self.y_start = display_size(self.m, self.n)
        self.color = random.choice(list(colors.keys()))

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            #Si ya acabó de resolver el laberinto un click en la pantalla lo devuelve al home page
            if self.solved_maze:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.__init__()
        return False

    def run_logic(self):

        if not self.solved_maze:
            if self.page == 'home':
                pass
            elif self.page == 'maze':
                pass

    def display_frame(self, screen):

        if self.solved_maze:
            font = pygame.font.SysFont("serif", 25) # Fuente
            text = font.render("Game Over, Click To Continue", True, (0, 0, 0)) # Texto
            center_x = (size[0] // 2) - (text.get_width() // 2) # posicion text
            center_y = (size[1] // 2) - (text.get_height() // 2)
            screen.blit(text, [center_x, center_y]) # ponerlo en pantalla

        if not self.solved_maze:   
            if self.page == 'home':
                #cargar imagenes y escalarlas
                home_view = pygame.image.load('static/images/home_view.png')
                home_view = pygame.transform.scale(home_view, size)
                screen.blit(home_view, [0, 0])
                
            elif self.page == 'maze':
            ##Mostramos el maze
                #cargar imagenes y escalarlas
                maze_view = pygame.image.load('static/images/maze_view.png')
                maze_view = pygame.transform.scale(maze_view, size)
                screen.blit(maze_view, [0, 0])
                
                #fondo
                maze_draw(screen, self.color, self.path, self.cell_size, self.x_start, self.y_start)
                
            ##Mostramos el menú si aún no se escogío un método
                if self.solve_method == '':
                    #cargar imagenes y escalarlas
                    menu = pygame.image.load('static/images/menu.png')
                    menu = pygame.transform.scale(menu, size)
                    screen.blit(menu, [0, 0])
                    
            ##Si no mostramos el método escogido
                else:
                    selected_method = pygame.image.load(f"static/images/resolverpor/{self.solve_method}.png")
                    selected_method = pygame.transform.scale(selected_method, (245, 130))
                    screen.blit(selected_method, [740, 156])
            
        pygame.display.flip()


def main():
    pygame.init()
    pygame.display.set_caption('Maze solver')

    #crear ventana
    screen = pygame.display.set_mode(size)
    #fps
    clock =  pygame.time.Clock()
    
    done = False
    game = Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
	main()