import csv

# Guarda el laberinto del archivo .csv en una lista de listas
def csv_to_list (path):
    maze = []
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row != []:
                maze.append(row)
    return maze

# Búsqueda en profundidad que recibe como argumentos la lista asociada al laberinto, la posición de inicio y la de salida
def depth_search(maze, start, end):
    solution = [start]
    path = [start]
    pos = start
    while pos != end:
        right = (pos[0],pos[1]+1)
        below = (pos[0]+1,pos[1])
        left = (pos[0],pos[1]-1)
        above = (pos[0]-1, pos[1])  
        if maze[right[0]][right[1]] == 'c' and right not in solution:
            pos = right
            path.append(right)
            solution.append(right)
        elif maze[below[0]][below[1]] == 'c' and below not in solution:
            pos = below
            path.append(below)
            solution.append(below)
        elif maze[left[0]][left[1]] == 'c' and left not in solution:
            pos = left
            path.append(left)
            solution.append(left)
        elif maze[above[0]][above[1]] == 'c' and above not in solution:
            pos = above
            path.append(above)
            solution.append(above)
        else:
            maze[pos[0]][pos[1]] = 'e';
            solution.remove(pos);
            pos = solution[len(path)-1]
    print(path)
    print(solution)
        