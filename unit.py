import pygame
import random

# Constantes
GRID_SIZE = 8
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
personnages = ["captain_america", "Hulk", "Ironman", "Spiderman", "Thor", "Hawkeye", "Wolverine", "Blackpanther", "Starlord", "Deadpool", "Torch", "JaneStorm", "Chose", "Drstrange"]


class Unit(pygame.sprite.Sprite):
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

    def __init__(self, x, y, health, attack_power, defense, team, size):
        super().__init__() #permet d'inialiser la classe sprite en appelant son constructeur avec super()
        """
        Construit une unité avec une position, une santé, une puissance d'attaque, une défense et une équipe.

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
        defense : int
            La capacité de résistance aux attaques

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
        self.size = size
        # pour générer l'image du joueur que l'on a choisi (Spiderman par exemple)
        self.image = pygame.image.load('Personnages/Deadpool.png')
        #self.image = self.get_image(95,0) # get image in this coordinate
        self.image = pygame.transform.scale(self.image,(32,32))
        self.image.set_colorkey([255,255,255]) # to remove the withe color of the background
        self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) #permet de générer un rectangle avec l'image que l'on pourra ensuite déplacer
    
    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        if 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE:
            self.x += dx
            self.y += dy

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health -= self.attack_power

    
    def soigner(self, target) :
        """soigner une unité ciblée"""
        if abs(self.x - target.x) <= 1 and abs(self.y - target.y) <= 1:
            target.health = self.health_max

    #def casser_mur(self, position) :
        #if position == position_obstacle :
            

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        color = BLUE if self.team == 'player' else RED
        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        #pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE //
                           #2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))

class captain_america :
    def __init__(self):
        self.health = 150
        self.move = 3
        self.defense = 90
        self.attack1 = "lancer_bouclier"
        self.attack_power1 = 20
        self.attack2 = "poings"
        self.attack_power2 = 10
        self.image = pygame.image.load("Personnages/CaptainAmerica.png").convert_alpha
    
class hulk :
    def __init__(self):
        self.health = 300
        self.move = 4
        self.defense = 90
        self.attack1 = "casser_les_murs"
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.image = pygame.image.load("Personnages/CaptainAmerica.png").convert_alpha