import pygame
import random

# Constantes
GRID_SIZE_x = 25
GRID_SIZE_y = 15
CELL_SIZE = 50
#CELL_SIZE = 60
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
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)



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
        name : str
            Le nom du personnage choisi
        x : int
            La position x du personnage sur la grille.
        y : int
            La position y du personnage sur la grille.
        health : int
            La santé du personnage
        move : int
            Le nombre de case maximum de déplacement du personnage
        defense : int
            La résistance du personnage aux attaques de l'ennemi
        attacks : liste de str
            La liste d'attaques du personnage.
        
     
       """
    def __init__(self, name, x, y, size, health, nbre_move, defense, attacks):
        super().__init__() #permet d'inialiser la classe sprite en appelant son constructeur avec super()
        self.name = name
        self.x = x # Position x du personnage
        self.y = y # Position y du personnage
        self.size = size # taille de l'image du personnage
        self.health = health
        self.nbre_move = nbre_move
        self.defense = defense
        self.attacks = attacks
        self.green_cases=[]

        # Liste des personnages 

        self.is_selected = False # variable servant dans la méthode draw() pour afficher le personnage
        
        # Liste des attaques
        self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", 
                         "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", 
                         "Boule_De_Feu", "Soigner", "Projectile" ]
        
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée

        self.distance_attack = 0
        self.max_health = 150
        self.health = 150
        
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


    def update_green_case(self,screen,player_units,enemy_units):
        self.green_cases=[] # réinitialisation des cases vertes pour ne pas avoir les anciennes
        self.green_cases.append((self.x, self.y)) # ajout de la case initial où le joueur se trouve

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
                    
                    # Si la case n'est pas occupée, ajoutez-la à la liste des cases vertes
                    if not case_occupée:
                        self.green_cases.append((green_x, green_y))
                    

    
    def draw_green_case(self, screen):
        color = GREEN
        for green_x,green_y in self.green_cases:
            pygame.draw.rect(screen, color, (green_x*CELL_SIZE, green_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Dessine les bords

    def attack(self, target):
        """Attaque une unité cible."""
        if abs(self.x - target.x) <= self.distance_attack and abs(self.y - target.y) <= self.distance_attack :
            target.health -= self.attack_power
    
    
    
          
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
        #personnage = random.choice(self.personnages) 
        #Pour générer l'image du joueur que l'on a choisi
        personnage = "Captain_America" 

        if personnage == "Captain_America" :
            #self.personnage.Captain_america()
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

            
        
        elif personnage == "Hulk" :
            self.personnage = Hulk()
            self.sprite_sheet = pygame.image.load('personnages/avengers2.jpg.png')
            self.image = self.get_image(52,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Ironman" :
            self.personnage = Ironman
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Spiderman" :
            self.personnage = Spiderman()
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Thor" :
            self.personage = Thor()
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Groot" :
            self.personnage = Groot()
            self.sprite_sheet = pygame.image.load('personnages/galaxy2.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Wolverine" :
            self.personnage = Wolverine()
            self.sprite_sheet = pygame.image.load('personnages/x_men.png')
            self.image = self.get_image(0,192) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Black_Panther" :
            self.personnage = Blackpanther()
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Starlord" :
            self.personnage = Starlord()
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Yondu" :
            self.personnage = Yondu()
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Torch" :
            self.personnage = Torch()
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(295, 193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Jane_Storm" :
            self.personnage = Janestorm()
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Chose" :
            self.personnage = Chose()
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(0,193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif personnage == "Dr_Strange" :
            self.personnage = Drstrange()
            self.sprite_sheet = pygame.image.load('personnages/doctor_strange.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))
        self.draw_health_bar(screen)
        

    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([52,52])
        image.blit(self.sprite_sheet,(10,0),(x,y,42,52))
        return image

    # Affichage de la barre de vie
    def draw_health_bar(self, surface):
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        bar_length = GRID_SIZE_x  # Longueur de la barre
        bar_height = 3   # Hauteur de la barre

        # Calcul de la largeur en fonction des PV
        fill = max(0, (self.health / self.max_health) * bar_length)

        # Position de la barre (juste au-dessus du personnage)
        bar_x = self.x
        bar_y = self.y 

        # Dessin de la barre de fond (contour)
        pygame.draw.rect(surface, BLACK, (bar_x*CELL_SIZE , bar_y*CELL_SIZE , bar_length + 2, bar_height + 2))
        # Dessin de la barre de vie actuelle
        pygame.draw.rect(surface, RED, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, bar_length, bar_height))  # Barre vide
        pygame.draw.rect(surface, GREEN, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, fill, bar_height))     # Barre remplie
    



#création de la classe de chaque personnage A CONFIRMER CAR PEUT-ETRE PAS NECESSAIRE

class Personnages (Unit) :
    def __init__(self):
        pass

    def Captain_america(self):
        self.health = 150
        self.nbre_move = 3
        self.defense = 90
        self.attaques = ["Poings","Lancer_bouclier" ]
        self.attack_power1 = 20
        self.distance_attack1 = 3
        self.attack2 = "poings"
        self.attack_power2 = 10
        self.distance_attack2 = 1
    
    def Hulk(self) :
        self.health = 300
        self.nbre_move = 4
        self.defense = 90
        self.attack1 = "casser_les_murs"
        self.distance_attack1 = 1
        self.attack2 = "poings"
        self.attack_power2 = 30
        self.distance_attack2 = 2


class Ironman (Unit) :
    def __init__(self):
        self.health = 150
        self.nbre_move = 8
        self.defense = 75
        self.attack1 = "laser"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "missile"
        self.attack_power2 = 40
        self.distance_attack2 = 5
        

class Spiderman(Unit) :
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
    

    def Thor(self) :
   
        self.health = 300
        self.move = 8
        self.defense = 75
        self.attack1 = "Marteau"
        self.attack_power1 = 50
        self.distance_attack1 = 5
        self.attack2 = "Foudre"
        self.attack_power2 = 60
        self.distance_attack2 = 3


class Groot(Unit) :
    def __init__(self):
        self.health = 150
        self.move = 3
        self.defense = 30
        self.attack1 = "Attaque_Branche"
        self.attack_power1 = 30
        self.distance_attack1 = 6
        self.attack2 = "Protection"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        

class Wolverine(Unit) :
    def __init__(self):
        self.health = 300
        self.move = 3
        self.defense = 75
        self.attack1 = "Griffes"
        self.attack_power1 = 60
        self.distance_attack1 = 2
        self.attack2 = "Poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1


class Blackpanther(Unit) :
    def __init__(self):
        self.health = 250
        self.move = 4
        self.defense = 30
        self.attack1 = "Griffes"
        self.attack_power1 = 50
        self.distance_attack1 = 2
        self.attack2 = "Poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
    

class Starlord :
    def __init__(self):
        self.health = 150
        self.move = 6
        self.defense = 30
        self.attack1 = "Pistolets"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "Poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        

class  Yondu(Unit):
    def __init__(self):
        self.health = 500
        self.move = 3
        self.defense = 50
        self.attack1 = "Fleche_Yaka"
        self.attack_power1 = 40
        self.distance_attack1 = 4
        self.attack2 = "Poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        

class Torch(Unit) :
    def __init__(self):
        self.health = 150
        self.move = 8
        self.defense = 40
        self.attack1 = "Boule_De_Feu"
        self.attack_power1 = 60
        self.distance_attack1 = 5
        self.attack2 = "Poings"
        self.attack_power2 = 40
        self.distance_attack2 = 1

class Janestorm(Unit) :
    def __init__(self):
        self.health = 100
        self.move = 3
        self.defense = 30
        self.attack1 = "Soigner"
        self.distance_attack1 = 3
        self.attack2 = "Poings"
        self.attack_power2 = 30
        self.distance_attack2 = 1
        

class Chose(Unit) :
    def __init__(self):
        self.health = 300
        self.move = 4
        self.defense = 80
        self.attack1 = "Casser_les_murs"
        self.distance_attack1 = 1
        self.attack2 = "Poings"
        self.attack_power2 = 40
        self.distance_attack2 = 2

class Drstrange(Unit) :
    def __init__(self):
        self.health = 150
        self.move = 6
        self.defense = 80
        self.attack1 = "Bloquer_adversaire"
        self.distance_attack1 = 4
        self.attack2 = "Projectiles"
        self.distance_attack2 = 5



#Création de la classe de chaque attaque
#attacks = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]

class Attacks(Personnages) :
    def __init__(self):
        pass

    def Poings(self) :
        self.power = 30
        self.quantite = 100
        self.distance = 1
       

class Griffes(Unit) :
    def __init__(self):
        self.power = 50
        self.quantite = 4
        self.distance = 3
        

class Lancer_bouclier(Unit) :
    def __init__(self):
        self.power = 40
        self.quantite = 3
        self.distance = 3
       

class Casser_les_murs(Unit) :
    def __init__(self):
        self.power = 60
        self.quantite = 2
        self.distance = 1
        

class Laser(Unit) :
    def __init__(self):
        self.power = 60
        self. quantite = 3
        self.distance = 5
        

class Missile :
    def __init__(self):
        self.power = 70
        self.quantite = 1
        self.distance = 6
        

class Bloquer_adversaire :
    def __init__(self):
        self.temps = 1
        self.power = 10
        self.quantite = 2
        self.distance = 4
        

class Attaque_toile :
    def __init__(self):
        self.power = 40
        self.quantite = 4
        self.distance = 3
        

class Marteau :
    def __init__(self):
        self.power = 50
        self.quantite = 2
        self.distance = 5
        
class Foudre :
    def __init__(self):
        self.power = 90
        self.quantite = 1
        self.distance = 6

class Attaque_branche :
    def __init__(self):
        self.power = 30
        self.quantite = 100
        self.distance = 3

class Protection :
    def __init__(self):
        self.power = 100
        self.temps = 1
        self.distance = 1

class Pistolets :
    def __init__(self):
        self.power = 40
        self.quantite = 10
        self.distance = 4

class Fleche_yaka :
    def __init__(self):
        self.power = 50
        self.quantite = 3
        self.distance = 5

class Boule_de_feu :
    def __init__(self):
        self.power = 60
        self.quantite = 3
        self.distance = 5

class Soigner :
    def __init__(self):
        self.power = 150
        self.quantite = 3
        self.distance = 1

class Projectile :
    def __init__(self):
        self.power = 50
        self.quantite = 4
        self.distance = 5





