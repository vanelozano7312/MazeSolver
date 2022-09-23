import csv, pygame
from colors import colors

#Función que dado un path de un archivo .csv retorna el tamaño (filas, columnas) del laberinto 
def mazesize(path):
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
# (está como si la pantalla default fuera de 700x700)
def displaysize(m, n):
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
def mazedraw(screen, color, path, cell_size, x_start, y_start):
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