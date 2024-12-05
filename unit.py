import pygame
import random
from attaque import *

# Constantes
GRID_SIZE_x = 25
GRID_SIZE_y=15
CELL_SIZE = 50

WIDTH = GRID_SIZE_x * CELL_SIZE
HEIGHT = GRID_SIZE_y * CELL_SIZE

#GRID_SIZE = 21.3

#WIDTH = GRID_SIZE * CELL_SIZE
#HEIGHT = GRID_SIZE * CELL_SIZE/(1.596)
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
LIGHT_GREEN = (50, 205, 50)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)




#self.attaques = ["Aucune_attaque","Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", 
                         #"Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", 
                         #"Boule_De_Feu", "Soigner", "Projectile" ]








class Unit():
    
    def __init__(self, name, x, y, size):
        super().__init__() #permet d'inialiser la classe sprite en appelant son constructeur avec super()
        self.name = name
        self.x = x # Position x du personnage
        self.y = y # Position y du personnage
        self.size = size # taille de l'image du personnage

        self.hero=hero
        
        self.green_cases=[]
        self.red_cases = []
        self.offsets = []
        self.is_selected = False # variable servant dans la méthode draw() pour afficher le personnage
        self.image = pygame.Surface(size)


 
 
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

    def update_green_case(self,player_units,enemy_units):
        self.green_cases=[] # réinitialisation des cases vertes pour ne pas avoir les anciennes
        self.green_cases.append((self.x, self.y)) # ajout de la case initial où le joueur se trouve
        
        self.cases=[] # cases obstacles
        # rivière 9-10
        for i in range(9,10+1):
            for j in range(0,9):
                self.cases.append((i,j)) 
        
 
        
        if self.is_selected:
            # Définir les déplacements possibles : orthogonaux + diagonales proches
            offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),(-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                (0, 0)] #la case ou se trouve déjà le personnage, au cas où il ne souhaite pas se déplacer

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
                    # TRoisieme verif cases obstacles
                    for x,y in self.cases:
                        if x==green_x and y==green_y:
                            case_occupée = True
                            break
                    
                    # Si la case n'est pas occupée, ajoutez-la à la liste des cases vertes
                    if not case_occupée:
                        self.green_cases.append((green_x, green_y))
    def draw_green_case(self, screen):
        color = BLUE
        for green_x,green_y in self.green_cases:
            pygame.draw.rect(screen, color, (green_x*CELL_SIZE, green_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Dessine les bords

    

    def update_red_case(self,attack):
        self.red_cases=[] # réinitialisation des cases vertes pour ne pas avoir les anciennes
        self.red_cases.append((self.x, self.y)) # ajout de la case initial où le joueur se trouve
        
        if attack == "Aucune action":
            self.attaque_selectionne = aucune_action

        if attack == "Poings" :
            self.attaque_selectionne = poings
        
        elif attack == "Griffes" :
            self.attaque_selectionne = griffes

        elif attack == "Lancer_bouclier" :
            self.attaque_selectionne = lancer_bouclier

        elif attack == "Casser_les_murs" :
            self.attaque_selectionne = casser_les_murs
        
        elif attack == "Laser" :
            self.attaque_selectionne = laser
        
        elif attack == "Missile":
            self.attaque_selectionne = missile
        
        elif attack == "Bloquer_adversaire":
            self.attaque_selectionne = bloquer_adversaire

        elif attack == "Attaque_toile":
            self.attaque_selectionne = attaque_toile
        
        elif attack == "Marteau":
            self.attaque_selectionne = marteau
        
        elif attack == "Foudre":
            self.attaque_selectionne = foudre
        
        elif attack == "Attaque_branche":
            self.attaque_selectionne = attaque_branche
        
        elif attack == "Protection":
            self.attaque_selectionne = protection
        
        elif attack == "Pistolets":
            self.attaque_selectionne = pistolets
        
        elif attack == "Fleche_Yaka":
            self.attaque_selectionne = fleche_yaka

        elif attack == "Boule_de_feu":
            self.attaque_selectionne = boule_de_feu

        elif attack == "Soigner":
            self.attaque_selectionne = soigner

        elif attack == "Projectile":
            self.attaque_selectionne = projectile

        if self.is_selected:
            # Définir les déplacements possibles : orthogonaux + diagonales proches
            #la case ou se trouve déjà le personnage, au cas où il ne souhaite pas se déplacer

            for dx, dy in self.attaque_selectionne.offsets:
                # Calcul des coordonnées de la case
                red_x = self.x + dx 
                red_y = self.y + dy

                # PREMIERE VERIFICATION: Vérifier que la case est dans les limites de la grille
                if 0 <= red_x < GRID_SIZE_x and 0 <= red_y < GRID_SIZE_y:
                    self.red_cases.append((red_x, red_y))
    def draw_red_case(self, screen):
        color = RED
        for red_x,red_y in self.red_cases:
            pygame.draw.rect(screen, color, (red_x*CELL_SIZE, red_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Dessine les bords
    
    
    
    def draw_perso(self, screen):
        """Affiche l'unité sur l'écran."""
         
        #Pour générer l'image du joueur que l'on a choisi
        personnage = self.name
        
        if personnage == "Captain_America" :
            
            self.personnage = captain_america
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

            
        
        elif personnage == "Hulk" :
            self.personnage = hulk
            self.sprite_sheet = pygame.image.load('personnages/avengers2.jpg.png')
            self.image = self.get_image(52,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Ironman" :
            self.personnage = ironman
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Spiderman" :
            
            self.personnage = spiderman
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Thor" :
            
            self.personnage = thor
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Groot" :
            
            self.personnage = groot
            self.sprite_sheet = pygame.image.load('personnages/galaxy2.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Wolverine" :
            
            self.personnage = wolverine
            self.sprite_sheet = pygame.image.load('personnages/x_men.png')
            self.image = self.get_image(0,192) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Black_Panther" :
            
            self.personnage = black_panther
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Starlord" :
            
            self.personnage = starlord
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Yondu" :
            
            self.personnage = yondu
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Torch" :
            
            self.personnage = torch
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(295, 193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Jane_Storm" :
            
            self.personnage = jane_storm
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Chose" :
            
            self.personnage = chose
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(0,193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Dr_Strange" :
            
            self.personnage = dr_strange
            self.sprite_sheet = pygame.image.load('personnages/doctor_strange.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

        self.health = self.personnage.health_max
        self.fill=self.health
        self.health_max = self.personnage.health_max
        self.nbre_move = self.personnage.nbre_move
        self.defense = self.personnage.defense
        self.attaques = self.personnage.attaques
        self.attack_power = self.personnage.attack_power
        

        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))
        #self.draw_health_bar(screen)
        
    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([52,52])
        image.blit(self.sprite_sheet,(10,0),(x,y,42,52))
        return image


    def update_health_bar(self): 
        bar_length = GRID_SIZE_x * 2 # Longueur de la barre 
        self.fill = (self.health / self.health_max) * bar_length  
    def draw_health_bar(self, screen):

        bar_length = GRID_SIZE_x * 2 # Longueur de la barre
        bar_height = 3   # Hauteur de la barre

        
        # Position de la barre (juste au-dessus du personnage)
        bar_x = self.x
        bar_y = self.y 

        # Dessin de la barre de fond (contour)
        pygame.draw.rect(screen, BLACK, (bar_x*CELL_SIZE , bar_y*CELL_SIZE , bar_length + 2, bar_height + 2))
        # Dessin de la barre de vie actuelle
        pygame.draw.rect(screen, RED, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, bar_length, bar_height))  # Barre vide
        pygame.draw.rect(screen, LIGHT_GREEN, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, self.fill, bar_height))     # Barre remplie
    


class Hero:
    def __init__(self, name, health, nbre_move, defense, attack_power, attaques):
        self.name = name
        self.health = health  # Santé actuelle
        self.nbre_move = nbre_move
        self.defense = defense
        self.attack_power = attack_power
        self.attaques = attaques  # Liste des attaques disponibles



# Instanciations des héros
captain_america = Hero(
    name="Captain America",
    health=1500,
    nbre_move=3,
    defense=75,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Lancer_bouclier"]
)

hulk = Hero(
    name="Hulk",
    health=300,
    nbre_move=4,
    defense=90,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Casser_les_murs"]
)

ironman = Hero(
    name="Ironman",
    health=150,
    nbre_move=8,
    defense=75,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Laser", "Missile"]
)

spiderman = Hero(
    name="Spiderman",
    health=150,
    nbre_move=6,
    defense=50,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Bloquer_adversaire", "Attaque_toile"]
)

thor = Hero(
    name="Thor",
    health=300,
    nbre_move=8,
    defense=75,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Marteau", "Foudre"]
)

groot = Hero(
    name="Groot",
    health=300,
    nbre_move=3,
    defense=30,
    attack_power=10,
    attaques=["Aucune action", "Attaque_branche", "Protection"]
)

wolverine = Hero(
    name="Wolverine",
    health=350,
    nbre_move=3,
    defense=75,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Griffes"]
)

black_panther = Hero(
    name="Black Panther",
    health=250,
    nbre_move=4,
    defense=30,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Griffes"]
)

starlord = Hero(
    name="Starlord",
    health=150,
    nbre_move=6,
    defense=30,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Pistolets"]
)

yondu = Hero(
    name="Yondu",
    health=300,
    nbre_move=3,
    defense=50,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Fleche_Yaka"]
)

torch = Hero(
    name="Torch",
    health=150,
    nbre_move=8,
    defense=40,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Boule_de_feu"]
)

jane_storm = Hero(
    name="Jane Storm",
    health=100,
    nbre_move=3,
    defense=30,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Soigner"]
)

chose = Hero(
    name="Chose",
    health=300,
    nbre_move=4,
    defense=80,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Casser_les_murs"]
)

dr_strange = Hero(
    name="Dr. Strange",
    health=150,
    nbre_move=6,
    defense=80,
    attack_power=10,
    attaques=["Aucune action", "Poings", "Bloquer_adversaire", "Projectiles"]
)

# Exemple d'accès aux héros test pour moi
all_heroes = [captain_america, hulk, ironman, spiderman, thor, groot, wolverine, 
              black_panther, starlord, yondu, torch, jane_storm, chose, dr_strange]

for hero in all_heroes:
    print(f"{hero.name}: {hero.health} HP, {hero.nbre_move} mouvements, Attaques: {', '.join(hero.attaques)}")

