import csv, pygame
from multiprocessing.connection import wait
import time
from data import colors
import shutil
import tkinter, os
import tkinter.filedialog

# Guarda el laberinto del archivo .csv en una lista de listas
def csv_to_list (path):
    maze = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row != []:
                maze.append(row)
    return maze

#Función que permite al usuario subir un archivo .csv y lo guarda en static/mazes/user_maze
def upload_maze():
    try:
        top = tkinter.Tk()
        top.withdraw()  
        file_name = tkinter.filedialog.askopenfilename(parent=top, title = "Select file",filetypes = (("csv files","*.csv"), ))
        shutil.copy(file_name, "./static/mazes/user_maze.csv")
        top.destroy()
    except:
        pass

#Función que dado un path de un archivo .csv retorna el tamaño (filas, columnas) del laberinto 
def maze_size(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        column_count = 0 
        for row in csv_reader:
            if row != []:
                # print(row)
                column_count = len(row)
                line_count += 1
        # print(f'Processed {line_count} lines and {row_count} rows.')
        return line_count, column_count


#Función que dada una matriz MxN calcula el tamaño de cada celda y el inicio en X y Y a dibujar
# (está como si la pantalla de juego default fuera de 700x700)
def display_size(m, n):
    if m>=n:
        cell_size = 700/m
        x_start = (700 - (n*cell_size))/2
        y_start = 0
    else:
        cell_size = 700/n
        y_start = (700 - (m*cell_size))/2
        x_start = 0
    return cell_size, x_start, y_start
    
    
#Función que dibuja el maze
# (está como si la pantalla default fuera de 700x700)
def maze_draw(screen, color, path, cell_size, x_start, y_start):
    pygame.draw.rect(screen, colors[color][1], (0, 0, 700, 700))
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        y = y_start
        for row in csv_reader:
            if row != []:
                x = x_start
                for cell in row:
                    if cell == 'w':
                        pygame.draw.rect(screen, colors[color][2], (x, y, cell_size, cell_size))
                    x = x + cell_size 
                y = y + cell_size
                
#Función que dibuja la solucion del maze
def maze_draw_solution(screen, color, cell_size, solution_path):
    if type(color[0]) != int :
        color = colors[color][0]
    if type(solution_path[0][0])!= int:
        for level in solution_path:
            for cell in level:
                pygame.draw.rect(screen, color, (cell_size*(cell[1]), cell_size*(cell[0]), cell_size, cell_size))
            pygame.time.wait(20)
            pygame.display.flip()
    else:
        for cell in solution_path:
            pygame.draw.rect(screen, color, (cell_size*(cell[1]), cell_size*(cell[0]), cell_size, cell_size))
            pygame.time.wait(20)
            pygame.display.flip()
            
#Función que dibuja el path del maze
def maze_draw_path(screen, color, cell_size, final_path):
    if type(color[0]) != int :
        color = colors[color][0]
    if type(final_path[0][0])!= int:
        for level in final_path:
            for cell in level:
                pygame.draw.rect(screen, color, (cell_size*(cell[1]), cell_size*(cell[0]), cell_size, cell_size))
    else:
        for cell in final_path:
            pygame.draw.rect(screen, color, (cell_size*(cell[1]), cell_size*(cell[0]), cell_size, cell_size))