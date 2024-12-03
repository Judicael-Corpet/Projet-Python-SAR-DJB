from unit import *
from menu import *
from game import *


import pygame
import heapq
import math
"""
class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)

    def is_walkable(self, x, y):
        Vérifie si une case est praticable.
        return (x, y) not in self.obstacles and 0 <= x < self.width and 0 <= y < self.height


import heapq
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
grid2 = grid


import heapq
for unit in self.game.player_units + self.game.enemy_units:
    grid[unit.x][unit.y] = 1
def a_star(grid, start, goal):
    def heuristic(a, b):
        # Distance de Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path  # Chemin trouvé

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Déplacements possibles
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    grid = grid2
    return None  # Aucun chemin trouvé


class Node:
    def __init__(self, position, parent=None):
        self.position = position  # Position sous forme de tuple (x, y)
        self.parent = parent      # Parent pour reconstituer le chemin
        self.g = float('inf')     # Coût du chemin actuel
        self.h = float('inf')     # Heuristique (distance estimée à la cible)
    
    def f(self):
        return self.g + self.h

class Grid:
    def __init__(self, width, height, obstacles=[]):
        self.width = width
        self.height = height
        self.obstacles = obstacles  # Liste de positions (x, y) bloquées

    def is_valid(self, x, y):
        #Vérifie si une position est valide (dans la grille et sans obstacle).
        return 0 <= x < self.width and 0 <= y < self.height and (x, y) not in self.obstacles

"""
"""
def a_star(grid, start, goal):
    
    Implémente A* pour trouver le chemin le plus court.
    :param grid: Instance de Grid.
    :param start: Tuple (x, y) de départ.
    :param goal: Tuple (x, y) cible.
    :return: Liste des positions (x, y) pour le chemin trouvé.
    
    open_nodes = []
    closed_nodes = {}
    start_node = Node(start)
    start_node.g = 0
    start_node.h = abs(start[0] - goal[0]) + abs(start[1] - goal[1])  # Heuristique de Manhattan
    open_nodes.append(start_node)
    print('salut la compagnie')
    while open_nodes:
        # Trouver le noeud avec le plus petit f()
        current_node = min(open_nodes, key=lambda n: n.f())
        open_nodes.remove(current_node)
        closed_nodes[current_node.position] = current_node

        # Si on atteint le but
        if current_node.position == goal:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Retourner le chemin dans l'ordre correct

        # Générer les successeurs
        x, y = current_node.position
        neighbors = [
            (x + dx, y + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ]
        print('salut la compagnie')
        for neighbor_pos in neighbors:
            if not grid.is_valid(*neighbor_pos) or neighbor_pos in closed_nodes:
                continue

            tentative_g = current_node.g + 1  # Coût de déplacement à la case voisine
            neighbor_node = Node(neighbor_pos, current_node)
            neighbor_node.g = tentative_g
            neighbor_node.h = abs(neighbor_pos[0] - goal[0]) + abs(neighbor_pos[1] - goal[1])

            # Ajouter à open_nodes s'il n'est pas déjà dedans ou si un meilleur chemin est trouvé
            existing_node = next((n for n in open_nodes if n.position == neighbor_pos), None)
            if existing_node is None or tentative_g < existing_node.g:
                if existing_node:
                    open_nodes.remove(existing_node)
                open_nodes.append(neighbor_node)

    return []  # Aucun chemin trouvé

"""


"""
class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.g_score = float('inf')  # Coût pour atteindre ce nœud
        self.h_score = 0  # Heuristique pour atteindre l'objectif
        self.f_score = float('inf')  # Coût total estimé

    def __lt__(self, other):
        return self.f_score < other.f_score

def heuristic(a, b):
    Distance de Manhattan pour une grille (si les déplacements diagonaux sont permis, utilisez euclidienne).
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def a_star(grid, start, goal):
    Implémente l'algorithme A* avec des optimisations de base.
    open_list = []
    closed_list = set()
    
    start_node = Node(start[0], start[1])
    start_node.g_score = 0
    start_node.h_score = heuristic(start_node, goal)
    start_node.f_score = start_node.g_score + start_node.h_score
    
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        # Vérifie si le point courant est le point d'arrivée
        if (current_node.x, current_node.y) == (goal.x, goal.y):
            path = []
            while current_node:
                path.append((current_node.x, current_node.y))
                current_node = current_node.parent
            return path[::-1]  # Retourne le chemin de départ à destination

        closed_list.add((current_node.x, current_node.y))

        # Explore les voisins (haut, bas, gauche, droite et diagonaux)
        neighbors = [
            (current_node.x - 1, current_node.y),  # gauche
            (current_node.x + 1, current_node.y),  # droite
            (current_node.x, current_node.y - 1),  # haut
            (current_node.x, current_node.y + 1),  # bas
            (current_node.x - 1, current_node.y - 1),  # diagonal haut-gauche
            (current_node.x + 1, current_node.y - 1),  # diagonal haut-droit
            (current_node.x - 1, current_node.y + 1),  # diagonal bas-gauche
            (current_node.x + 1, current_node.y + 1)   # diagonal bas-droit
        ]

        for nx, ny in neighbors:
            if not grid.is_walkable(nx, ny):
                continue

            if (nx, ny) in closed_list:
                continue

            neighbor_node = Node(nx, ny, current_node)
            tentative_g_score = current_node.g_score + (1 if nx == current_node.x or ny == current_node.y else math.sqrt(2))  # Coût de 1 pour les mouvements orthogonaux, sqrt(2) pour diagonaux

            # Si le chemin trouvé est meilleur, on met à jour le nœud
            if tentative_g_score < neighbor_node.g_score:
                neighbor_node.g_score = tentative_g_score
                neighbor_node.h_score = heuristic(neighbor_node, goal)
                neighbor_node.f_score = neighbor_node.g_score + neighbor_node.h_score

                if not any((neighbor_node.x, neighbor_node.y) == (n.x, n.y) for n in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # Retourne None si aucun chemin n'est trouvé


"""









"""
#def handle_enemy_turn(self):
        #IA très simple pour les ennemis.
       
        
        for enemy in self.enemy_units:
            # Déplacement aléatoire
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            # Attaque si possible
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)
            
        
            for enemy in self.enemy_units:
                target_x_1 = self.player_units[0].x
                target_y_1 = self.player_units[0].y
                target_vie_1 = self.player_units[0].health
                target_x_2 = self.player_units[1].x
                target_y_2 = self.player_units[1].y
                target_vie_2 = self.player_units[1].health
                # DEPLACEMENT
                if np.sqrt((target_x_1 - enemy.x)**2+(target_y_1 - enemy.y)**2) < np.sqrt((target_x_2 - enemy.x)**2+(target_y_2 - enemy.y)**2) :
                    target_x = self.player_units[0].x
                    target_y = self.player_units[0].y


                    # ATTAQUE
                    if np.sqrt((target_x_1 - enemy.x)**2+(target_y_1 - enemy.y)**2) == np.sqrt((target_x_2 - enemy.x)**2+(target_y_2 - enemy.y)**2) :
                        if target_vie_1 < target_vie_2 :
                            pass #attaquer le 1




    def handle_enemy_turn(self):
        for enemy in self.enemy_units:
            enemy.is_selected  = True
            enemy.update_green_case(self.player_units,self.enemy_units) 
            # Déterminer la cible la plus proche
            target_1 = self.player_units[0]
            target_2 = self.player_units[1]
            dist_1 = np.sqrt((target_1.x - enemy.x) ** 2 + (target_1.y - enemy.y) ** 2)
            dist_2 = np.sqrt((target_2.x - enemy.x) ** 2 + (target_2.y - enemy.y) ** 2)
            target = target_1 if dist_1 < dist_2 else target_2

            # Appliquer A* pour trouver le chemin vers la cible
            grid = Grid(self.grid_width, self.grid_height, self.obstacles)
            path = a_star(grid, (enemy.x, enemy.y), (target.x, target.y))

            # Déplacer l'ennemi d'une étape sur le chemin
            if path and len(path) > 1:
                next_step = path[1]  # Le premier élément est la position actuelle
                enemy.x, enemy.y = next_step

            # Si l'ennemi est à portée, attaquer
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)
            enemy.is_selected = False


"""


"""
import heapq

grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]


def a_star(grid, start, goal):
    def heuristic(a, b):
        # Distance de Manhattan            
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(grid), len(grid[0])
    open_set = []        
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path  # Chemin trouvé

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Déplacements possibles
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None  # Aucun chemin trouvé


start = (0, 0)
goal = (5, 5)
path = a_star(grid, start, goal)
print("Chemin trouvé:", path if path else "Aucun chemin trouvé")




from collections import deque

from collections import deque

def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Vérifier si les points de départ et d'arrivée sont valides
    if not (0 <= start[0] < rows and 0 <= start[1] < cols) or grid[start[0]][start[1]] == 1:
        print("Point de départ invalide.")
        return None
    if not (0 <= goal[0] < rows and 0 <= goal[1] < cols) or grid[goal[0]][goal[1]] == 1:
        print("Point d'arrivée invalide.")
        return None

    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            # Construire le chemin à partir du dictionnaire `came_from`
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        # Vérifier les voisins
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols  # Dans les limites de la grille
                    and grid[neighbor[0]][neighbor[1]] == 0           # Pas un obstacle
                    and neighbor not in came_from):                  # Pas déjà visité
                queue.append(neighbor)
                came_from[neighbor] = current

    print("Aucun chemin trouvé.")
    return None
# Exemple d'utilisation
grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1],
]

start = (16, 9)
goal = (0, 0)

path = bfs(grid, start, goal)
if path:
    print("Chemin trouvé :", path)
else:
    print("Aucun chemin trouvé.")
    
grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1],
]


start = (16, 9)
goal = (0, 0)

import heapq

def a_star(grid, start, goal):
    def heuristic(a, b):
        #Distance de Manhattan pour estimer le coût restant.
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(grid), len(grid[0])
    open_set = []  # File de priorité
    heapq.heappush(open_set, (0, start))  # Ajoute la case de départ avec un score f=0
    came_from = {}  # Garde une trace des déplacements
    g_score = {start: 0}  # Coût pour atteindre un nœud
    f_score = {start: heuristic(start, goal)}  # Score total estimé (g + h)

    while open_set:
        _, current = heapq.heappop(open_set)  # Récupère le nœud avec le plus faible f_score

        print(f"Exploring node: {current}")

        # Si on atteint l'objectif
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)  # Inclut le point de départ
            path.reverse()  # Retourne le chemin
            return path  # Retourne le chemin trouvé

        # Explore les voisins (haut, bas, gauche, droite)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Vérifie si le voisin est dans la grille et accessible
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] != 1:
                cost = 1
                if grid[neighbor[0]][neighbor[1]] == 2:
                    cost = 0.1  # Coût réduit pour les chemins spéciaux

                tentative_g_score = g_score[current] + cost  # Coût d'un pas supplémentaire

                # Si le coût pour atteindre ce voisin est meilleur, on met à jour
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                    # Ajouter à l'open_set si pas déjà présent
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))
                        print(f"Adding neighbor: {neighbor} with f_score: {f_score[neighbor]}")

    return None  # Aucun chemin trouvé
"""

