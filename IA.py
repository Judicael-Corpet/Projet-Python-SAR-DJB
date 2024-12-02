from unit import *
from menu import *
from game import *



import heapq
import math

class Grid:
    def __init__(self, width, height, obstacles):
        self.width = width
        self.height = height
        self.obstacles = set(obstacles)

    def is_walkable(self, x, y):
        """Vérifie si une case est praticable."""
        return (x, y) not in self.obstacles and 0 <= x < self.width and 0 <= y < self.height


"""
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
    """Distance de Manhattan pour une grille (si les déplacements diagonaux sont permis, utilisez euclidienne)."""
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)


def a_star(grid, start, goal):
    """Implémente l'algorithme A* avec des optimisations de base."""
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