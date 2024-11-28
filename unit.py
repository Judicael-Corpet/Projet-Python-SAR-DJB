import pygame
import random

# Constantes
GRID_SIZE = 21.3
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE/(1.596)
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Hawkeye", "Wolverine", "Black_Panther", "Starlord", "Deadpool", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]


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
    def __init__(self, x, y, team, size):
        super().__init__() #permet d'inialiser la classe sprite en appelant son constructeur avec super()
        self.x = x
        self.y = y
        self.team = team  # 'player' ou 'enemy'
        self.is_selected = False
        self.size = size
        self.image = pygame.Surface(size)

        #Pour générer l'image du joueur que l'on a choisi

        self.personnage = "Ironman" #random.choice(personnages)

        if self.personnage == "Captain_America" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            #self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object
        

        elif self.personnage == "Hulk" :
            self.sprite_sheet = pygame.image.load('personnages/avengers2.jpg.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Ironman" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(90,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Spiderman" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object
        
        elif self.personnage == "Thor" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Hawkeye" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Wolverine" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Black_Panther" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Starlord" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Deadpool" :
            self.isprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Torch" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Jane_Storm" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Chose" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

        elif self.personnage == "Dr_Strange" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object

    def move(self, dx, dy):
        """Déplace l'unité de dx, dy."""
        if 0 <= self.x + dx < GRID_SIZE and 0 <= self.y + dy < GRID_SIZE: # boundary
            self.x += dx
            self.y += dy

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
        #pygame.draw.circle(screen, color, (self.x * CELL_SIZE + CELL_SIZE //
                           #2, self.y * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))

    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([42,52])
        image.blit(self.sprite_sheet,(10,0),(x,y,42,52))
        return image

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