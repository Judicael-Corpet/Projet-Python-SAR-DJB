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
personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Hawkeye", "Wolverine", "Black_Panther", "Starlord", "Deadpool", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]


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

    def __init__(self, x, y, team, size):
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
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False
        self.size = size
        # pour générer l'image du joueur que l'on a choisi (Deadpool par exemple)
        
        self.personnage = random.choice(personnages)
        if self.personnage == "Captain_America" :
            self.image = pygame.image.load('Personnages/CaptainAmerica.png')

        elif self.personnage == "Hulk" :
            self.image = pygame.image.load('Personnages/Hulk.png.jpg')

        elif self.personnage == "Ironman" :
            self.image = pygame.image.load('Personnages/Ironman.png')

        elif self.personnage == "Spiderman" :
            self.image = pygame.image.load('Personnages/spiderman.png')
        
        elif self.personnage == "Thor" :
            self.image = pygame.image.load('Personnages/Thor1.png')

        elif self.personnage == "Hawkeye" :
            self.image = pygame.image.load('Personnages/Hawkeye1.png.jpg')

        elif self.personnage == "Wolverine" :
            self.image = pygame.image.load('Personnages/Wolverine.png')

        elif self.personnage == "Black_Panther" :
            self.image = pygame.image.load('Personnages/Blackpanther.png')

        elif self.personnage == "Starlord" :
            self.image = pygame.image.load('Personnages/Starlord.png')

        elif self.personnage == "Deadpool" :
            self.image = pygame.image.load('Personnages/Deadpool.png')

        elif self.personnage == "Torch" :
            self.image = pygame.image.load('Personnages/Toch1.png')

        elif self.personnage == "Jane_Storm" :
            self.image = pygame.image.load('Personnages/JaneStorm.png')

        elif self.personnage == "Chose" :
            self.image = pygame.image.load('Personnages/Chose1.png')

        elif self.personnage == "Dr_Strange" :
            self.image = pygame.image.load('Personnages/Drstrange.png')

   
        self.image = pygame.transform.scale(self.image,self.size)
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


#création de la classe de chaque personnage
class captain_america :
    def __init__(self):
        self.health = 150
        self.move = 3
        self.defense = 90
        self.attack1 = "lancer_bouclier"
        self.attack_power1 = 20
        self.distance_attack1 = 3
        self.attack2 = "poings"
        self.attack_power2 = 10
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/CaptainAmerica.png").convert_alpha
    
class hulk :
    def __init__(self):
        self.health = 300
        self.move = 4
        self.defense = 90
        self.attack1 = "casser_les_murs"
        self.distance_attack1 = 1
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 2
        self.image = pygame.image.load("Personnages/Hulk.png").convert_alpha

class ironman :
    def __init__(self):
        self.health = 150
        self.move = 8
        self.defense = 75
        self.attack1 = "laser"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "missile"
        self.attack_power2 = 40
        self.distance_attack2 = 5
        self.image = pygame.image.load("Personnages/Ironman.png").convert_alpha

class Spiderman :
    def __init__(self):
        self.health = 100
        self.move = 6
        self.defense = 50
        self.attack1 = "bloquer_adversaire"
        self.attack_power1 = 20
        self.distance_attack1 = 4
        self.attack2 = "attaque_toile"
        self.attack_power2 = 40
        self.distance_attack2 = 3
        self.image = pygame.image.load("Personnages/Spiderman.png").convert_alpha

class Thor :
    def __init__(self):
        self.health = 300
        self.move = 8
        self.defense = 75
        self.attack1 = "marteau"
        self.attack_power1 = 50
        self.distance_attack1 = 5
        self.attack2 = "foudre"
        self.attack_power2 = 60
        self.distance_attack2 = 3
        self.image = pygame.image.load("Personnages/Thor1.png").convert_alpha

class hawkeye :
    def __init__(self):
        self.health = 150
        self.move = 3
        self.defense = 30
        self.attack1 = "fleches"
        self.attack_power1 = 30
        self.distance_attack1 = 6
        self.attack2 = "sabre"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Hawkeye.png").convert_alpha

class wolverine :
    def __init__(self):
        self.health = 300
        self.move = 3
        self.defense = 75
        self.attack1 = "griffes"
        self.attack_power1 = 60
        self.distance_attack1 = 2
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Wolverine.png").convert_alpha

class blackpanther :
    def __init__(self):
        self.health = 250
        self.move = 4
        self.defense = 30
        self.attack1 = "griffes"
        self.attack_power1 = 50
        self.distance_attack1 = 2
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Blackpanther.png").convert_alpha

class starlord :
    def __init__(self):
        self.health = 150
        self.move = 6
        self.defense = 30
        self.attack1 = "pistolets"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Starlord.png").convert_alpha

class deadpool :
    def __init__(self):
        self.health = 500
        self.move = 3
        self.defense = 50
        self.attack1 = "pistolets"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Deadpool.png").convert_alpha

class torche :
    def __init__(self):
        self.health = 150
        self.move = 8
        self.defense = 40
        self.attack1 = "boule de feu"
        self.attack_power1 = 60
        self.distance_attack1 = 5
        self.attack2 = "poings"
        self.attack_power2 = 40
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/Toch1.png").convert_alpha

class janestorm :
    def __init__(self):
        self.health = 100
        self.move = 3
        self.defense = 30
        self.attack1 = "soigner"
        self.distance_attack1 = 3
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        self.image = pygame.image.load("Personnages/JaneStorm.png").convert_alpha

class chose :
    def __init__(self):
        self.health = 300
        self.move = 4
        self.defense = 80
        self.attack1 = "casser_les_murs"
        self.distance_attack1 = 1
        self.attack2 = "poings"
        self.attack_power2 = 40
        self.distance_attack2 = 2
        self.image = pygame.image.load("Personnages/Chose1.png").convert_alpha

class drstrange :
    def __init__(self):
        self.health = 150
        self.move = 6
        self.defense = 80
        self.attack1 = "bloquer_adversaire"
        self.attack_power1 = 30
        self.distance_attack1 = 4
        self.attack2 = "projectiles"
        self.attack_power2 = 40
        self.distance_attack2 = 5
        self.image = pygame.image.load("Personnages/Drstange.png").convert_alpha
