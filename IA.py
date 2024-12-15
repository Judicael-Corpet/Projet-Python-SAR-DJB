



grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

#36 colonnes
#19 lignes


def a_star(grid, start, goal):
    """
    Implémente l'algorithme A* pour trouver le chemin optimal.
    :param grid: La grille où 1 représente un obstacle et 0 une case libre.
    :param start: Coordonnées de départ (x, y).
    :param goal: Coordonnées d'arrivée (x, y).
    :return: Liste des étapes du chemin trouvé, ou [] si aucun chemin n'est possible.
    """
    def heuristic(a, b):
        # Distance de Manhattan
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def get_neighbors(node):
        # Retourne les voisins valides (dans la grille et non-obstacles)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Haut, Droite, Bas, Gauche
        neighbors = []
        for dx, dy in directions:
            nx, ny = node[0] + dx, node[1] + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == 0:
                neighbors.append((nx, ny))
        return neighbors

    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruire le chemin
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor in get_neighbors(current):
            tentative_g_score = g_score[current] + 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return []  # Aucun chemin trouvé






def handle_enemy_turn(self):
        for enemy in self.enemy_units:
            enemy.is_selected = True
            enemy.update_green_case(self.player_units, self.enemy_units)
            print(enemy)
            # Déterminer la cible la plus proche
            target_1 = self.player_units[0]
            target_2 = self.player_units[1]
            dist_1 = np.sqrt((target_1.x - enemy.x) ** 2 + (target_1.y - enemy.y) ** 2)
            dist_2 = np.sqrt((target_2.x - enemy.x) ** 2 + (target_2.y - enemy.y) ** 2)
            target = target_1 if dist_1 < dist_2 else target_2

            # Mise à jour de la grille avec les positions des unités comme obstacles
            current_grid = [row[:] for row in grid]  # Copie de la grille
            for unit in self.player_units + self.enemy_units:
                print(unit.x)
                print(unit.y)
                current_grid[unit.y][unit.x] = 1  # Marquer les cases occupées comme obstacles

            # Appliquer A* pour trouver le chemin vers la cible
            start = (enemy.x, enemy.y)
            goal = (target.x, target.y)

            path = a_star(current_grid, start, goal)
            print(f"Path found: {path}")
            
            if path and len(path) > 1:
                next_step = path[1]  # Le prochain pas après la position actuelle
                enemy.x, enemy.y = next_step
                print(f"Enemy moved to {next_step}")
            else:
                print(f"No path found for enemy at {start}")
            
            print(path)
            # Déplacer l'ennemi d'une étape sur le chemin
            if path and len(path) > 1:
                next_step = path[0]  # Le premier élément est la position actuelle
                enemy.x, enemy.y = next_step
                print('deplacement')
            else:
                print("Aucun chemin trouvé pour l'ennemi :", enemy)
            
            # Attaque si possible
            """
            player_selected = target.attribuer_class_perso() 
            #choix d'une attaque
            if abs(enemy.x - player_selected.x) <= enemy.distance_maxi_attack and abs(enemy.y - player_selected.y) <= enemy.distance_maxi_attack :
                enemy_attack = random.choice(target.list_attaques[1:])
                indice = target.list_attaques.index(enemy_attack)
                print (f"indice pour l'attaque enemy est {indice}" )
                enemy_attack_selected = target.attribuer_class_attaque(indice) 
                print (f"l'attaque enemy est {enemy_attack_selected.name}")
                player_health = self.target_health
                print (f"MA VIE NE TIENT QU'A {player_health}")
                new_player_health = target.eni_attack(enemy_attack_selected, player_selected, player_health)
                self.target_health = new_player_health
                print (f"QUE TREPAS SI JE FAIS BLI {new_player_health}")
            else :
                enemy_attack_selected = Aucune_action()
                print("J'ai choisi de ne pas attaquer")

                player_health = self.target_health
            
            if player_health <= 0:
                print(f"{target.name} est mort")
                self.player_units.remove(target)
            """
            self.flip_display()

            enemy.is_selected = False
            pygame.time.wait(1000)
        play = True
        return play, self.list_player_health







import heapq  # Pour la gestion de la file de priorité

def heuristic(pos1, pos2):
    """Heuristique de Manhattan pour A* (distance en cases)."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def get_neighbors(position, green_cases):
    """Retourne les voisins accessibles depuis une position donnée."""
    x, y = position
    potential_neighbors = [
        (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)  # Cases adjacentes
    ]
    return [case for case in potential_neighbors if case in green_cases]
def find_best_path(start, goal, green_cases):
    """Trouve le chemin le plus court vers la cible (goal) en respectant les cases vertes."""
    # Utilisation d'A* (A-star)
    open_set = []  # Cases à explorer (file de priorité)
    heapq.heappush(open_set, (0, start))  # (coût estimé, position)

    came_from = {}  # Pour suivre le chemin
    g_score = {start: 0}  # Coût réel pour atteindre une case
    f_score = {start: heuristic(start, goal)}  # Coût total estimé

    while open_set:
            # Case avec le coût estimé le plus bas
        _, current = heapq.heappop(open_set)

            # Si on atteint la cible, reconstruire le chemin
        if current == goal:
            return reconstruct_path(came_from, current)

        # Explorer les voisins accessibles
        neighbors = get_neighbors(current, green_cases)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1  # Coût d'un pas

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # Mieux vaut passer par ce chemin
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

        # Si aucun chemin n'est trouvé, retourner la position de départ
    return [start]


def reconstruct_path(came_from, current):
    """Reconstruction du chemin à partir des cases explorées."""
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path





green_cases = enemy.update_green_case(self.player_units, self.enemy_units)
            start = (enemy.x, enemy.y)  # Position de départ
            goal = (target.x, target.y)  # Position de la cible
            path = find_best_path(start, goal, green_cases)


if len(path) > 1:  # Si un mouvement est possible
                next_step = path[1]  # Prochaine case sur le chemin
                dx, dy = next_step[0] - enemy.x, next_step[1] - enemy.y
                enemy.move(dx, dy)