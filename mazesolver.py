import pygame, sys, random
from mazeprocess import *
from data import *
from button import Button
from algorithms import *
import time

size = (1000, 700)

class Game(object):
    
    def __init__(self):
        self.path = ''
        self.solved_maze = False
        self.solving = False
        self.solution_path = []
        self.final_path=[]
        self.solving_time=0
        self.checked_cells = 0
        self.page = 'home'              #posibles páginas: home, maze
        self.solve_method =''          #posibles methods: a:anchura, ae:a*, bdcu:búsqeda de costo uniforme, bg:búsqueda greedy
                                        #p: profundidad, pi:profundidad iterativa, st: search tree ,'': no se ha escogido
        
        ##Creamos todos los botones necesarios y los inicializamos
        self.upload_maze = Button(images_data['upload_maze'][0], images_data['upload_maze'][1], 'upload_maze')
        self.b_5x5 = Button(images_data['maze_size_buttons'][0], images_data['maze_size_buttons'][1][0], 'b_5x5')
        self.b_10x10 = Button(images_data['maze_size_buttons'][0], images_data['maze_size_buttons'][1][1], 'b_10x10')
        self.b_50x50 = Button(images_data['maze_size_buttons'][0], images_data['maze_size_buttons'][1][2], 'b_50x50')
        self.b_100x100 = Button(images_data['maze_size_buttons'][0], images_data['maze_size_buttons'][1][3], 'b_100x100')
        self.b_menu = Button(images_data['menu'][0], images_data['menu'][1], 'b_menu')
        self.b_p = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][0], 'b_p')
        self.b_a = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][1], 'b_a')
        self.b_pi = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][2], 'b_pi')
        self.b_bdcu = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][3], 'b_bdcu')
        self.b_bg = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][4], 'b_bg')
        self.b_ae = Button(images_data['menu_buttons'][0], images_data['menu_buttons'][1][5], 'b_ae')
        self.b_home = Button(images_data['home'][0], images_data['home'][1], 'b_home')
        self.b_run = Button(images_data['runmaze'][0], images_data['runmaze'][1], 'b_run')
        
        self.click_upload_maze = False
        self.click_b_5x5 = False
        self.click_b_10x10 = False
        self.click_b_50x50 = False
        self.click_b_100x100 = False
        self.click_b_menu = False
        self.click_b_p = False
        self.click_b_a = False
        self.click_b_pi = False
        self.click_b_bdcu = False
        self.click_b_bg = False
        self.click_b_ae = False
        self.click_b_home = False
        self.click_b_run = False
        

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

            #Mira si algún botón válido ha sido presionado
            if self.page == 'home':
                self.click_upload_maze = self.upload_maze.button_pressed(event)
                self.click_b_5x5 = self.b_5x5.button_pressed(event)
                self.click_b_10x10 = self.b_10x10.button_pressed(event)
                self.click_b_50x50 = self.b_50x50.button_pressed(event)
                self.click_b_100x100 = self.b_100x100.button_pressed(event)
                
            elif self.page == 'maze':
                self.click_b_menu = self.b_menu.button_pressed(event)
                self.click_b_home = self.b_home.button_pressed(event)
                
                if self.solve_method == '':
                    self.click_b_p = self.b_p.button_pressed(event)
                    self.click_b_a = self.b_a.button_pressed(event)
                    self.click_b_pi = self.b_pi.button_pressed(event)
                    self.click_b_bdcu = self.b_bdcu.button_pressed(event)
                    self.click_b_bg = self.b_bg.button_pressed(event)
                    self.click_b_ae = self.b_ae.button_pressed(event)
                else:
                    self.click_b_run = self.b_run.button_pressed(event) 
        return False

    
    def run_logic(self):

        if self.page == 'home':
                if self.click_upload_maze or self.click_b_5x5 or self.click_b_10x10 or self.click_b_50x50 or self.click_b_100x100:
                    if self.click_upload_maze:
                        upload_maze()
                        self.path = 'static/mazes/user_maze.csv'
                    elif self.click_b_5x5:
                        self.path = 'static/mazes/maze_5x5.csv'
                    elif self.click_b_10x10:
                        self.path = 'static/mazes/maze_10x10.csv'
                    elif self.click_b_50x50:
                        self.path = 'static/mazes/maze_50x50.csv'
                    elif self.click_b_100x100:
                        self.path = 'static/mazes/maze_100x100.csv'
                        
                    self.m, self.n = maze_size(self.path)          #tamaño mxn del maze
                    self.cell_size, self.x_start, self.y_start = display_size(self.m, self.n)
                    self.color = random.choice(list(colors.keys()))
                    self.page = 'maze'
                   
        elif self.page == 'maze':
            if self.click_b_home:
                self.__init__()
                    
            if self.solve_method == '':
                if self.click_b_p:
                    self.solve_method = 'p'
                elif self.click_b_a:
                    self.solve_method = 'a'
                elif self.click_b_pi:
                    self.solve_method = 'pi'
                elif self.click_b_bdcu:
                    self.solve_method = 'bdcu'
                elif self.click_b_bg:
                    self.solve_method = 'bg'
                elif self.click_b_ae:
                    self.solve_method = 'ae'
            else:                   
                if self.click_b_menu and not self.solving:
                    self.solved_maze = False
                    self.solving = False
                    self.solution_path = []
                    self.final_path=[]
                    self.solving_time=0
                    self.checked_cells = 0
                    self.solve_method =''    
                    self.click_b_p = False
                    self.click_b_a = False
                    self.click_b_pi = False
                    self.click_b_bdcu = False
                    self.click_b_bg = False
                    self.click_b_ae = False
                elif self.click_b_run and not self.solving:
                    self.solved_maze = False
                    self.solving = not self.solving
                    start, end = 0, 0
                    start = time.time()
                    if self.solve_method == 'p':
                        self.solution_path, self.final_path = depth_search((0,1), (self.m-1, self.n-2), self.path)
                    elif self.solve_method == 'a':
                        self.solution_path, self.final_path = breadth_search((0,1), (self.m-1, self.n-2), self.path)
                    elif self.solve_method == 'pi':
                        self.solution_path, self.final_path = iterative_depth((0,1), (self.m-1, self.n-2), self.path)
                    elif self.solve_method == 'bdcu':
                        self.solution_path, self.final_path = uniform_cost_search((0,1), (self.m-1, self.n-2), self.path)
                    elif self.solve_method == 'bg':
                        self.solution_path, self.final_path = greedy_search((0,1), (self.m-1, self.n-2), self.path)
                    elif self.solve_method == 'ae':
                        self.solution_path, self.final_path = a_star_search((0,1), (self.m-1, self.n-2), self.path)
                    end = time.time()
                    self.solving_time = end - start
                    self.path_cell = 0
                    self.solution_cell = 0
                    self.solved_maze = True
                    self.checked_cells = checked_cells(self.solution_path)
                    
    
    def display_frame(self, screen):

        if self.page == 'home':
            #cargar imagenes y escalarlas
            home_view = pygame.image.load('static/images/home_view.png')
            home_view = pygame.transform.scale(home_view, size)
            screen.blit(home_view, [0, 0])
            self.upload_maze.draw(screen)
            self.b_5x5.draw(screen)
            self.b_10x10.draw(screen)
            self.b_50x50.draw(screen)
            self.b_100x100.draw(screen)
                
        elif self.page == 'maze':        
        ##Mostramos el maze
            #cargar imagenes y escalarlas
            maze_view = pygame.image.load('static/images/maze_view.png')
            maze_view = pygame.transform.scale(maze_view, size)
            screen.blit(maze_view, [0, 0])
            
            #fondo
            maze_draw(screen, self.color, self.path, self.cell_size, self.x_start, self.y_start)
            if not self.solving:
                self.b_run.draw(screen)
                
        ##Mostramos el menú si aún no se escogió un método
            if self.solve_method == '':
                #cargar imagenes y escalarlas
                menu = pygame.image.load('static/images/menu.png')
                menu = pygame.transform.scale(menu, size)
                screen.blit(menu, [0, 0])
                self.b_p.draw(screen)
                self.b_a.draw(screen)
                self.b_pi.draw(screen)
                self.b_bdcu.draw(screen)
                self.b_bg.draw(screen)
                self.b_ae.draw(screen)
                
            else:
                ##Si no mostramos el método escogido
                selected_method = pygame.image.load(f"static/images/resolverpor/{self.solve_method}.png")
                selected_method = pygame.transform.scale(selected_method, images_data['selected_method'][0])
                screen.blit(selected_method, images_data['selected_method'][1])
                
                #Si se está resolviendo dibuja una a una las casillas 
                if self.solving:
                    maze_draw_solution(screen, self.color, self.cell_size, self.solution_path)
                    self.solving = False
                else:
                    self.b_menu.draw(screen)
                    
                #Si ya se resolvió muestra la solución en blanco y en amarillo el path final
                if self.solved_maze:
                    maze_draw_path(screen, (255, 255, 255), self.cell_size, self.solution_path)
                    maze_draw_path(screen, (255, 222, 0), self.cell_size, self.final_path)
                    
                    #Mostramos el tiempo
                    time = pygame.image.load("static/images/tiempo.png")
                    time = pygame.transform.scale(time, images_data['time'][0])
                    screen.blit(time, images_data['time'][1])
                    font = pygame.font.SysFont("serif", 25) # Fuente
                    text = font.render(f"{self.solving_time}", True, (255, 255, 255))
                    screen.blit(text, (864, 393)) # ponerlo en pantalla
                    
                    #Mostramos las celdas revisadas
                    cells = pygame.image.load("static/images/celdasrevisadas.png")
                    cells = pygame.transform.scale(cells, images_data['cells'][0])
                    screen.blit(cells, images_data['cells'][1])
                    font = pygame.font.SysFont("serif", 25) # Fuente
                    text = font.render(f"{self.checked_cells}", True, (255, 255, 255))
                    screen.blit(text, (840, 530)) # ponerlo en pantalla
            
            self.b_home.draw(screen)
        
        pygame.display.flip()
    
  
def main():
    pygame.init()
    pygame.display.set_caption('Maze solver')

    #crear ventana
    screen = pygame.display.set_mode(size)
    #crear ventana para el search tree
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