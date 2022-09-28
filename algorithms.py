import csv
from mazeprocess import csv_to_list

# Búsqueda en profundidad que recibe como argumentos la lista asociada al laberinto, la posición de inicio y la de salida
def depth_search(start, end, file):
    maze = csv_to_list(file)
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
            pos = solution[len(solution)-1]
    return path, solution
