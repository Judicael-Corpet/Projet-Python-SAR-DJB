import pygame
import random

# Constantes

GRID_SIZE_x = 40
GRID_SIZE_y=25
CELL_SIZE = 32
WIDTH = GRID_SIZE_x * CELL_SIZE
HEIGHT = GRID_SIZE_y * CELL_SIZE
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class Unit:
    """
    Classe pour représenter une unité.

    ...
    Attributs
    ---------
    x : int
        La position x de l'unité sur la grille.
    y : int
        La position y de l'unité sur la grille.
    health : int
        La santé de l'unité.
    attack_power : int
        La puissance d'attaque de l'unité.
    defense : int
    team : str
        L'équipe de l'unité ('player' ou 'enemy').
    is_selected : bool
        Si l'unité est sélectionnée ou non.

    Méthodes
    --------
    move(dx, dy)
        Déplace l'unité de dx, dy.
    attack(target)
        Attaque une unité cible.
    draw(screen)
        Dessine l'unité sur la grille.
    """

    def __init__(self, x, y, health, attack_power, defense, team):
        """
        Construit une unité avec une position, une santé, une puissance d'attaque et une équipe.

        Paramètres
        ----------
        x : int
            La position x de l'unité sur la grille.
        y : int
            La position y de l'unité sur la grille.
        health : int
            La santé de l'unité.
        attack_power : int
            La puissance d'attaque de l'unité.
        team : str
            L'équipe de l'unité ('player' ou 'enemy').
        """
        self.x = x
        self.y = y
        self.health = health
        self.attack_power = attack_power
        self.team = team  # 'player' ou 'enemy'
        self.defense = defense
        self.is_selected = False
        self.green_cases=[]
    

    def move(self, dx, dy):
        """Déplace l'unité de dx, dy, uniquement si la case cible est valide."""
        # Calcul de la position cible
        target_x = self.x + dx
        target_y = self.y + dy

        # Vérifie si la position cible est dans les cases vertes
        print(self.green_cases)
        if (target_x, target_y) in self.green_cases:
            self.x = target_x
            self.y = target_y
        else:
            print("Déplacement invalide : en dehors des cases autorisées.")


    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power
          
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        color = BLUE if self.team == 'player' else RED
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE //
                           2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
    
    def update_green_case(self,screen,player_units,enemy_units):
        self.green_cases=[] # réinitialisation des cases vertes pour ne pas avoir les anciennes
        self.green_cases.append((self.x, self.y)) # ajout de la case initial où le joueur se trouve

        if self.is_selected:
            # Définir les déplacements possibles : orthogonaux + diagonales proches
            offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonales proches
            ]

            for dx, dy in offsets:
                # Calcul des coordonnées de la case
                green_x = self.x + dx # pas encore implementer dans la liste qui dessine les cases
                green_y = self.y + dy

                # PREMIERE VERIFICATION: Vérifier que la case est dans les limites de la grille
                if 0 <= green_x < GRID_SIZE_x and 0 <= green_y < GRID_SIZE_y:
                    #DEUXIEME VERIFICATION: Vérifier si la case est occupée par une unité (joueur ou ennemi)
                    case_occupée = False
                    for unit in player_units + enemy_units:
                        if unit.x == green_x and unit.y == green_y:
                            case_occupée = True
                            break
                    
                    # Si la case n'est pas occupée, ajoutez-la à la liste des cases vertes
                    if not case_occupée:
                        self.green_cases.append((green_x, green_y))
                    

    
    def draw_green_case(self, screen):
        color = GREEN
        for green_x,green_y in self.green_cases:
            pygame.draw.rect(screen, color, (green_x*CELL_SIZE, green_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Dessine les bords
