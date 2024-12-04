import pygame
import random


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



class Unit():
    
    def __init__(self, name, x, y, size):#, health, nbre_move, defense, attacks):
        super().__init__() #permet d'inialiser la classe sprite en appelant son constructeur avec super()
        self.name = name
        self.x = x # Position x du personnage
        self.y = y # Position y du personnage
        self.size = size # taille de l'image du personnage
        self.max_health = 150
        self.health = 0
        self.nbre_move = 0
        self.defense = 0
        self.attaques = []
        self.distance_attack = 0
        self.attack_power = 0
        self.red_cases = []
        self.health_max = 150
        #self.attaque_selectionne = Aucune_action()
        self.offsets = []
        self.attaque_selectionne = "Aucune Action"
        self.is_selected = False # variable servant dans la méthode draw() pour afficher le personnage
        
        # Liste des attaques
        #self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", 
                         #"Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", 
                         #"Boule_De_Feu", "Soigner", "Projectile" ]
        
        self.attaque_selectionne_index = 0  # Indice de l'attaque sélectionnée

        
        
        self.image = pygame.Surface(size)

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
        color = GREEN
        for green_x,green_y in self.green_cases:
            pygame.draw.rect(screen, color, (green_x*CELL_SIZE, green_y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)  # Dessine les bords


    def update_red_case(self,attack):
        self.red_cases=[] # réinitialisation des cases vertes pour ne pas avoir les anciennes
        self.red_cases.append((self.x, self.y)) # ajout de la case initial où le joueur se trouve
        
        if attack == "Aucune action":
            self.attaque_selectionne = Aucune_action()

        if attack == "Poings" :
            self.attaque_selectionne = Poings()
        
        elif attack == "Griffes" :
            self.attaque_selectionne = Griffes()

        elif attack == "Lancer_bouclier" :
            self.attaque_selectionne = Lancer_bouclier()

        elif attack == "Casser_les_murs" :
            self.attaque_selectionne = Casser_les_murs()
        
        elif attack == "Laser" :
            self.attaque_selectionne = Laser()
        
        elif attack == "Missile":
            self.attaque_selectionne = Missile()
        
        elif attack == "Bloquer_adversaire":
            self.attaque_selectionne = Bloquer_adversaire()

        elif attack == "Attaque_toile":
            self.attaque_selectionne = Attaque_toile()
        
        elif attack == "Marteau":
            self.attaque_selectionne = Marteau()
        
        elif attack == "Foudre":
            self.attaque_selectionne = Foudre()
        
        elif attack == "Attaque_branche":
            self.attaque_selectionne = Attaque_branche()
        
        elif attack == "Protection":
            self.attaque_selectionne = Protection()
        
        elif attack == "Pistolets":
            self.attaque_selectionne = Pistolets()
        
        elif attack == "Fleche_Yaka":
            self.attaque_selectionne = Fleche_yaka()

        elif attack == "Boule_de_feu":
            self.attaque_selectionne = Boule_de_feu()

        elif attack == "Soigner":
            self.attaque_selectionne = Soigner()

        elif attack == "Projectile":
            self.attaque_selectionne = Projectile()

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
    
    
    
    def attack(self, type_attack, target):
        """Attaque une unité cible.

        if type_attack == "Aucune Action" :
            self.attaque_selectionne = Aucune_action()
        
        elif type_attack == "Poings" :
            self.attaque_selectionne = Poings()
        
        elif type_attack == "Griffes" :
            self.attaque_selectionne = Griffes()

        elif type_attack == "Lancer_bouclier" :
            self.attaque_selectionne = Lancer_bouclier()

        elif type_attack == "Casser_les_murs" :
            self.attaque_selectionne = Casser_les_murs()
        
        elif type_attack == "Laser" :
            self.attaque_selectionne = Laser()
        
        elif type_attack == "Missile":
            self.attaque_selectionne = Missile()
        
        elif type_attack == "Bloquer_adversaire":
            self.attaque_selectionne = Bloquer_adversaire()

        elif type_attack == "Attaque_toile":
            self.attaque_selectionne = Attaque_toile()
        
        elif type_attack == "Marteau":
            self.attaque_selectionne = Marteau()
        
        elif type_attack == "Foudre":
            self.attaque_selectionne = Foudre()
        
        elif type_attack == "Attaque_branche":
            self.attaque_selectionne = Attaque_branche()
        
        elif type_attack == "Protection":
            self.attaque_selectionne = Protection()
        
        elif type_attack == "Pistolets":
            self.attaque_selectionne = Pistolets()
        
        elif type_attack == "Fleche_Yaka":
            self.attaque_selectionne = Fleche_yaka()

        elif type_attack == "Boule_de_feu":
            self.attaque_selectionne = Boule_de_feu()

        elif type_attack == "Soigner":
            self.attaque_selectionne = Soigner()

        elif type_attack == "Projectile":
            self.attaque_selectionne = Projectile()
        """

        #print (f"Lattaque selectionnee pour la methode attack {self.attaque_selectionne.name}")
        for red_x, red_y in self.red_cases :
            if target.x == red_x and  target.y == red_y :
                target.health = target.health - type_attack.attack_power*type_attack.precision*(target.defense/100)
        return target.health
    
                #target.healthlf.attaque_selectionne.attack_power*precision*(1-target.defense)          self.attaque_selectionne.distance_attack



#self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", 
                         #"Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", 
                         #"Boule_De_Feu", "Soigner", "Projectile" ]
    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
         
        #Pour générer l'image du joueur que l'on a choisi
        personnage = self.name
        
        if personnage == "Captain_America" :
            
            self.personnage = Captain_america()
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
            self.personnage = Ironman()
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
            
            self.personnage = Thor()
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
            
            self.personnage = Black_panther()
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
            
            self.personnage = Jane_storm()
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
            
            self.personnage = Dr_strange()
            self.sprite_sheet = pygame.image.load('personnages/doctor_strange.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

        self.health = self.personnage.health
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

    # Affichage de la barre de vie
    #def update_health_bar(self, screen, unit) :
        #new_health = unit.health

    
    def draw_health_bar(self, screen):
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        bar_length = GRID_SIZE_x * 2 # Longueur de la barre
        bar_height = 3   # Hauteur de la barre

        # Calcul de la largeur en fonction des PV
        fill = (self.health / self.health_max) * bar_length

        # Position de la barre (juste au-dessus du personnage)
        bar_x = self.x
        bar_y = self.y 

        # Dessin de la barre de fond (contour)
        pygame.draw.rect(screen, BLACK, (bar_x*CELL_SIZE , bar_y*CELL_SIZE , bar_length + 2, bar_height + 2))
        # Dessin de la barre de vie actuelle
        pygame.draw.rect(screen, RED, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, bar_length, bar_height))  # Barre vide
        pygame.draw.rect(screen, LIGHT_GREEN, (bar_x*CELL_SIZE, bar_y*CELL_SIZE, fill, bar_height))     # Barre remplie
    

    
#création de la classe de chaque personnage A CONFIRMER CAR PEUT-ETRE PAS NECESSAIRE



class Captain_america(Unit):
    def __init__(self):
        self.health = 1500
        self.health_max = 1500
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Lancer_bouclier" ]
        
    
class Hulk(Unit) :
    def __init__(self):
        self.health = 300
        self.health_max = 300
        self.nbre_move = 4
        self.defense = 90
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings", "casser_les_murs"]


class Ironman (Unit) :
    def __init__(self):
        self.health = 150
        self.health_max = 150
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","laser", "missile"]
    
        

class Spiderman(Unit) :
    def __init__(self):
        self.health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 50
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","bloquer_adversaire", "attaque_toile"]
    
    

class Thor(Unit) :
    def __init__(self) :
        self.health = 300
        self.health_max = 300
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Marteau", "Foudre"]
    


class Groot(Unit) :
    def __init__(self):
        self.health = 300
        self.health_max = 300
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.attaques = ["Aucune action","Attaque_branche", "Protection"]
    
        

class Wolverine(Unit) :
    def __init__(self):   
        self.health = 300
        self.health_max = 350
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Griffes"]
    


class Black_panther(Unit) :
    def __init__(self):
        self.health = 250
        self.health_max = 250
        self.nbre_move = 4
        self.defense = 30
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Griffes"]
    
    

class Starlord (Unit) :
    def __init__(self):
        self.health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 30
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Pistolets"]
    
        

class  Yondu(Unit):
    def __init__(self):
        self.health = 300
        self.health_max = 300
        self.nbre_move = 3
        self.defense = 50
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Fleche_Yaka"]
    
        

class Torch(Unit) :
    def __init__(self):
        self.health = 150
        self.health_max = 150
        self.nbre_move = 8
        self.defense = 40
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Boule_de_feu"]
        

class Jane_storm(Unit) :
    def __init__(self):
        self.health = 100
        self.health_max = 100
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Soigner"]
    
        

class Chose(Unit) :
    def __init__(self):
        self.health = 300
        self.health_max = 300
        self.nbre_move = 4
        self.defense = 80
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Casser_les_murs"]
    

class Dr_strange(Unit) :
    def __init__(self):
        self.health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 80
        self.attack_power = 10
        self.attaques = ["Aucune action", "Poings","Bloquer_adversaire","Projectiles" ]
    



#Création de la classe de chaque attaque
#attacks = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]

#class Attacks(Unit) :
    #def __init__(self):
    #    pass

class Aucune_action(Unit) :
    def __init__(self) :
        self.name = "Aucune action"
        self.offsets = [
                (0, 0),  # Diagonales proches
                ]
        self.attack_power = 0
        self.quantite = 100
        self.distance_attack = 1
        self.precision = 0

    def utiliser (self, cible) :
        
        damage = 0
        cible.take_damage(damage)

class Poings(Unit) :
    def __init__(self) :
        self.name = "Poings"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 70
        self.quantite = 100
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health

class Griffes(Unit) :
    def __init__(self):
        self.name = "Griffes"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 90
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Lancer_bouclier(Unit) :
    def __init__(self):
        self.name = "Lancer_bouclier"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 90
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
       

class Casser_les_murs(Unit) :
    def __init__(self):
        self.name = "Casser_les_murs"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 100
        self.quantite = 1
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Laser(Unit) :
    def __init__(self):
        self.name = "Laser"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 100
        self. quantite = 1
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Missile (Unit):
    def __init__(self):
        self.name = "Missile"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 130
        self.quantite = 1
        self.distance_attack = 6
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Bloquer_adversaire (Unit):
    def __init__(self):
        self.name = "Bloquer_adversaire"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.temps = 3
        self.attack_power = 100
        self.quantite = 2
        self.distance_attack = 4
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Attaque_toile (Unit):
    def __init__(self):
        self.name = "Attaque_toile"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 90
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Marteau (Unit):
    def __init__(self):
        self.name = "Marteau"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 130
        self.quantite = 2
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        
class Foudre (Unit):
    def __init__(self):
        self.name = "Foudre"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 150
        self.quantite = 1
        self.distance_attack = 6
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Attaque_branche(Unit) :
    def __init__(self):
        self.name = "Attaque_branche"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 100
        self.quantite = 100
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Protection (Unit):
    def __init__(self):
        self.name = "Protection"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 150
        self.temps = 1
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Pistolets(Unit) :
    def __init__(self):
        self.name = "Pistolets"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 120
        self.quantite = 10
        self.distance_attack = 4
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Fleche_yaka(Unit) :
    def __init__(self):
        self.name = "Fleche_Yaka"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 150
        self.quantite = 3
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Boule_de_feu (Unit):
    def __init__(self):
        self.name = "Boule_de_feu"
        self.offsets = [(-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 150
        self.quantite = 3
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        

class Soigner (Unit):
    def __init__(self):
        self.name = "Soigner"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 150
        self.quantite = 3
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health

class Projectile(Unit) :
    def __init__(self):
        self.name = "Projectile"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 100
        self.quantite = 3
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
#hero = Unit("Captain_America",0,0,[55,55])
#mechant = Unit("Hulk",0,0,[55,55])
#hero.attack("Poings", mechant)




