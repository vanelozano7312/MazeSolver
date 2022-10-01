import csv
from mazeprocess import csv_to_list
import queue

# Clase usada para guardar tanto coordenadas como nodo padre, esta es usada en Breadth, Uniform Cost y A*
class Node:
    def __init__(self,coord,parent):
        self.coord = coord
        self.parent = parent
    
#Esta función toma la coordenada de un nodo, un padre y un laberinto en forma matricial y devuelve la expancion de este nodo como lista de coordenadas
def expand(node,parent,maze):
    exp = []
    if (node[0],node[1]+1) != parent and maze[node[0]][node[1]+1] == 'c':
        exp.append((node[0],node[1]+1))
    if (node[0]+1,node[1]) != parent and maze[node[0]+1][node[1]] == 'c':
        exp.append((node[0]+1,node[1]))
    if (node[0],node[1]-1) != parent and maze[node[0]][node[1]-1] == 'c':
        exp.append((node[0],node[1]-1))
    if (node[0]-1,node[1]) != parent and maze[node[0]-1][node[1]] == 'c':
        exp.append((node[0]-1,node[1]))
    return exp

#Esta función toma una lista de alcanzados y una coordenada de inicio y devuelve una lista de nodos alcanzados solo con coordenadas y una lista del camino optimo a tomar
def normal (reached,start):
    solution = []
    for x in reached:
        solution.append(x.coord)
    path = []
    node = reached[len(reached)-1]
    while node.coord != start:
        path.append(node.coord)
        node = node.parent
    path.append(start)
    path.reverse()
    return [solution,path]

#Heuristica para la función de busqueda A*
def star_heuristic(coord,end):
    return (end[0]-coord[0])+(end[1]-coord[1])

#Busqueda en anchura, recibe como argumentos la posicion de inicio, fin, y el archivo asociado al laberinto
def breadth_search(start,end,path):
    maze = csv_to_list (path)
    reached = []
    goal = True
    frontier = queue.Queue()
    ndstart = Node(start,Node((-1,-1),(-1,-1)))
    frontier.put(ndstart)
    while goal and (not frontier.empty()):
        node = frontier.get()
        reached.append(node)
        for x in expand(node.coord,node.parent.coord,maze):
            frontier.put(Node(x,node))
            if x == end:
                goal = False
                break
    while not frontier.empty():
        reached.append(frontier.get())
    if goal:
        print(-1)
        print(-1)
        return [-1,-1]
    tmp = normal(reached,start)
    solution = tmp[0]
    path = tmp[1]
    return solution, path

#Busqueda de costo uniforme, recibe como parametros posicion de inicio, fin, y archivo asociado al laberinto
def uniform_cost_search(start,end,path):
    i = 1
    maze = csv_to_list(path)
    reached = []
    goal = True
    frontier = queue.PriorityQueue()
    ndstart = Node(start,Node((-1,-1),(-1,-1)))
    frontier.put((1,i,ndstart))
    while goal and (not frontier.empty()):
        node = frontier.get()
        if node[2].coord not in reached:
            reached.append(node[2])
            for x in expand(node[2].coord,node[2].parent.coord,maze):
                i = i+1
                if x == end:
                    goal = False
                    finisher = Node(x,node[2])
                    break
                frontier.put((node[0]+1,i,Node(x,node[2])))
    while not frontier.empty():
        node = frontier.get()
        if node[2].coord not in reached:
            reached.append(node[2])
    reached.append(finisher)
    if goal:
        print(-1)
        print(-1)
        return [-1,-1]
    tmp = normal(reached,start)
    solution = tmp[0]
    path = tmp[1]
    return solution, path

#Busqueda A*, recibe lo mismo que todos los demas a este punto
def a_star_search(start,end,path):
    i = 1
    maze = csv_to_list(path)
    reached = []
    goal = True
    frontier = queue.PriorityQueue()
    ndstart = Node(start,Node((-1,-1),(-1,-1)))
    frontier.put((1+star_heuristic(start,end),1,i,ndstart))
    while goal and (not frontier.empty()):
        node = frontier.get()
        g = node[1]+1
        if node[3].coord not in reached:
            reached.append(node[3])
            for x in expand(node[3].coord,node[3].parent.coord,maze):
                i = i+1
                if x == end:
                    goal = False
                    finisher = Node(x,node[3])
                    break
                frontier.put((g+star_heuristic(node[3].coord,end),g,i,Node(x,node[3])))
    while not frontier.empty():
        node = frontier.get()
        if node[3].coord not in reached:
            reached.append(node[3])
    reached.append(finisher)
    if goal:
        print(-1)
        print(-1)
        return [-1,-1]
    tmp = normal(reached,start)
    solution = tmp[0]
    path = tmp[1]
    return solution, path

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
            maze[pos[0]][pos[1]] = 'e'
            solution.remove(pos)
            pos = solution[len(solution)-1]
    return path, solution
