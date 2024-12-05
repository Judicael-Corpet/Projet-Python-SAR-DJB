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
        self.cases=[]
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
        
         # cases obstacles
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
                    for player in player_units + enemy_units:
                        if player.x == green_x and player.y == green_y:
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
        
        if attack == "Aucune Action":
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
    
    
    
    def attack(self, type_attack, target, target_health):
        """Attaque une unité cible."""
        #target_health = target.get_health()
        #print (f"Lattaque selectionnee pour la methode attack {self.attaque_selectionne.name}")
        for red_x, red_y in self.red_cases :
            if target.x == red_x and  target.y == red_y :
                
                print(f"la cible de mon attaque est  : {target.name}, elle a {target_health} points de vie, et une défense de {target.defense}, end = "" ")
                print(f"l'attaque j'ai choisie est {type_attack} avec une puissance de {type_attack.attack_power}et une précision de {type_attack.precision}")
                  
                target_health = target_health - type_attack.attack_power*type_attack.precision*(1 - target.defense/100)/type_attack.distance_attack
                print (f"IL NE TE RESTE PLUS QUE {target_health} POINT DE VIE AVANT DE MOURIRR !!!! HAHAHAHAHAHHAHAHAHAHAH")
            else :
                target_health = target_health
        return target_health
    

    def draw(self, screen):
        """Affiche l'unité sur l'écran."""
         
        #Pour générer l'image du joueur que l'on a choisi
        
        
        if self.name == "Captain_America" :   
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

            
        
        elif self.name == "Hulk" :           
            self.sprite_sheet = pygame.image.load('personnages/avengers2.jpg.png')
            self.image = self.get_image(52,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Ironman" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Spiderman" :
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Thor" :
            self.sprite_sheet = pygame.image.load('personnages/avengers.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Groot" :       
            self.sprite_sheet = pygame.image.load('personnages/galaxy2.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Wolverine" :
            self.sprite_sheet = pygame.image.load('personnages/x_men.png')
            self.image = self.get_image(0,192) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Black_Panther" :           
            self.sprite_sheet = pygame.image.load('personnages/avengers3.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Starlord" :
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Yondu" :
            self.sprite_sheet = pygame.image.load('personnages/galaxy.png')
            self.image = self.get_image(295,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Torch" :
        
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(295, 193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Jane_Storm" :
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(150,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Chose" :
            self.sprite_sheet = pygame.image.load('personnages/4_fantastic.png')
            self.image = self.get_image(0,193) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
            
        elif self.name == "Dr_Strange" :
            self.sprite_sheet = pygame.image.load('personnages/doctor_strange.png')
            self.image = self.get_image(0,0) # get image in this coordinate
            self.image = pygame.transform.scale(self.image,self.size)
            self.image.set_colorkey([0,0,0]) # to remove the withe color of the background

        if self.is_selected:
            pygame.draw.rect(screen, GREEN, (self.x * CELL_SIZE,
                             self.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            
        screen.blit(self.image, (self.x*CELL_SIZE, self.y*CELL_SIZE))
        
        
    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([52,52])
        image.blit(self.sprite_sheet,(10,0),(x,y,42,52))
        return image

    # Affichage de la barre de vie
    #def update_health_bar(self, screen, self) :
        #new_health = self.health

    
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
    
    def attribuer_class_perso(self) :
        if self.name == "Captain_America" : 
            perso = perso_Captain_america(self.x,self.y,self.size)            
        elif self.name == "Hulk" :
            perso = perso_Hulk(self.x,self.y,self.size)           
        elif self.name == "Ironman" :
            perso = perso_Ironman(self.x,self.y,self.size)           
        elif self.name == "Spiderman" :
            perso = perso_Spiderman(self.x,self.y,self.size)           
        elif self.name == "Thor" :
            perso = perso_Thor(self.x,self.y,self.size)           
        elif self.name == "Groot" : 
            perso = perso_Groot(self.x,self.y,self.size)            
        elif self.name == "Wolverine" :
            perso = perso_Wolverine(self.x,self.y,self.size)            
        elif self.name == "Black_Panther" :
            perso = perso_Black_panther(self.x,self.y,self.size)           
        elif self.name == "Starlord" :
            perso = perso_Starlord(self.x,self.y,self.size)           
        elif self.name == "Yondu" :
            perso = perso_Yondu(self.x,self.y,self.size)           
        elif self.name == "Torch" : 
            perso = perso_Torch(self.x,self.y,self.size)           
        elif self.name == "Jane_Storm" :
            perso = perso_Jane_storm(self.x,self.y,self.size)           
        elif self.name == "Chose" :    
            perso = perso_Chose(self.x,self.y,self.size)            
        elif self.name == "Dr_Strange" :
            perso = perso_Dr_strange(self.x,self.y,self.size)
        else:
            raise ValueError(f"Personnage non reconnu : {self.name}")
        return perso
#création de la classe de chaque personnage A CONFIRMER CAR PEUT-ETRE PAS NECESSAIRE

    def attribuer_class_attaque(self, indice) :
        if self.list_attaques[indice] == "Aucune Action" :
            attaque_selectionne = Aucune_action()
                                
        elif self.list_attaques[indice] == "Poings" :
            attaque_selectionne = Poings()
        
        elif self.list_attaques[indice] == "Griffes" :
            attaque_selectionne = Griffes()

        elif self.list_attaques[indice] == "Lancer_bouclier" :
            attaque_selectionne = Lancer_bouclier()

        elif self.list_attaques[indice] == "Casser_les_murs" :
            attaque_selectionne = Casser_les_murs()
        
        elif self.list_attaques[indice] == "Laser" :
            attaque_selectionne = Laser()
        
        elif self.list_attaques[indice] == "Missile":
            attaque_selectionne = Missile()
        
        elif self.list_attaques[indice] == "Bloquer_adversaire":
            attaque_selectionne = Bloquer_adversaire()

        elif self.list_attaques[indice] == "Attaque_toile":
            attaque_selectionne = Attaque_toile()
        
        elif self.list_attaques[indice] == "Marteau":
            attaque_selectionne = Marteau()
        
        elif self.list_attaques[indice] == "Foudre":
            attaque_selectionne = Foudre()
        
        elif self.list_attaques[indice] == "Attaque_branche":
            attaque_selectionne = Attaque_branche()
        
        elif self.list_attaques[indice] == "Protection":
            attaque_selectionne = Protection()
        
        elif self.list_attaques[indice] == "Pistolets":
            attaque_selectionne = Pistolets()
        
        elif self.list_attaques[indice] == "Fleche_Yaka":
            attaque_selectionne = Fleche_yaka()

        elif self.list_attaques[indice] == "Boule_de_feu":
            attaque_selectionne = Boule_de_feu()

        elif self.list_attaques[indice] == "Soigner":
            attaque_selectionne = Soigner()

        elif self.list_attaques[indice] == "Projectile":
            attaque_selectionne = Projectile()
        else:
            raise ValueError(f"attaque non reconnu : {self.list_attaques[indice]}")
        return attaque_selectionne

class perso_Captain_america(Unit):
    def __init__(self, x, y, size):
        super().__init__("Captain_America", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Lancer_bouclier" ]

    def get_health (self):
        return self.__health    
    
class perso_Hulk(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Hulk", x, y, size)
        self.__health = 300
        self.health_max = 300
        self.nbre_move = 4
        self.defense = 90
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings", "Casser_les_murs"]

    def get_health (self):
        return self.__health

class perso_Ironman (Unit) :
    def __init__(self, x, y, size):
        super().__init__("Ironman", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Laser", "Missile"]

    def get_health (self):
        return self.__health    
        

class perso_Spiderman(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Spiderman", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 50
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Bloquer_adversaire", "Attaque_toile"]

    def get_health (self):
        return self.__health    
    

class perso_Thor(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Thor", x, y, size)
        self.__health = 300
        self.health_max = 300
        self.nbre_move = 8
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Marteau", "Foudre"]
    
    def get_health (self):
        return self.__health

class perso_Groot(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Groot", x, y, size)
        self.__health = 300
        self.health_max = 300
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["Aucune Action","Attaque_branche", "Protection"]
    
    def get_health (self):
        return self.__health
        

class perso_Wolverine(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Wolverine", x, y, size)   
        self.__health = 300
        self.health_max = 350
        self.nbre_move = 3
        self.defense = 75
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Griffes"]

    def get_health (self):
        return self.__health    


class perso_Black_panther(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Black_Panther", x, y, size)
        self.__health = 250
        self.health_max = 250
        self.nbre_move = 4
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Griffes"]

    def get_health (self):
        return self.__health    
    

class perso_Starlord (Unit) :
    def __init__(self, x, y, size):
        super().__init__("Starlord", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Pistolets"]

    def get_health (self):
        return self.__health    
        

class  perso_Yondu(Unit):
    def __init__(self, x, y, size):
        super().__init__("Yondu", x, y, size)
        self.__health = 300
        self.health_max = 300
        self.nbre_move = 3
        self.defense = 50
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Fleche_Yaka"]

    def get_health (self):
        return self.__health    
        

class perso_Torch(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Torch", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 8
        self.defense = 40
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Boule_de_feu"]

    def get_health (self):
        return self.__health        

class perso_Jane_storm(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Jane_Storm", x, y, size)
        self.__health = 100
        self.health_max = 100
        self.nbre_move = 3
        self.defense = 30
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Soigner"]

    def get_health (self):
        return self.__health    
        

class perso_Chose(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Chose", x, y, size)
        self.__health = 300
        self.health_max = 300
        self.nbre_move = 4
        self.defense = 80
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Casser_les_murs"]

    def get_health (self):
        return self.__health    

class perso_Dr_strange(Unit) :
    def __init__(self, x, y, size):
        super().__init__("Dr_Strange", x, y, size)
        self.__health = 150
        self.health_max = 150
        self.nbre_move = 6
        self.defense = 80
        self.attack_power = 10
        self.list_attaques = ["Aucune Action", "Poings","Bloquer_adversaire","Projectiles" ]

    def get_health (self):
        return self.__health



#Création de la classe de chaque attaque
#attacks = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]

#class Attacks(Unit) :
    #def __init__(self):
    #    pass

class Aucune_action(Unit) :
    def __init__(self) :
        self.name = "Aucune Action"
        self.offsets = [
                (0, 0),  # Diagonales proches
                ]
        self.attack_power = 0
        self.quantite = 100
        self.distance_attack = 1
        self.precision = 0
class Poings(Unit) :
    def __init__(self) :
        self.name = "Poings"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Diagonales proches
                ]
        self.attack_power = 30
        self.quantite = 100
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

class Griffes(Unit) :
    def __init__(self):
        self.name = "Griffes"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                (-2, 0), (2, 0), (0, -2), (0, 2) ]
        self.attack_power = 60
        self.quantite = 3
        self.distance_attack = 2
        self.precision = random.uniform(0.5, 1)

class Lancer_bouclier(Unit) :
    def __init__(self):
        self.name = "Lancer_bouclier"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1),  # Diagonales proches
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, -1), (-2, 1), (2, -1), (2, 1)]
        self.attack_power = 50
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)
 

class Casser_les_murs(Unit) :
    def __init__(self):
        self.name = "Casser_les_murs"
        self.offsets = [
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Diagonales proches
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
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)    # Diagonales proches
                ]
        self.attack_power = 100
        self. quantite = 1
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)
        
class Missile (Unit):
    def __init__(self):
        self.name = "Missile"
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, -1), (2, -1), (-1, -2), (-1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Diagonales proches
                ]
        self.attack_power = 110
        self.quantite = 1
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)

    def utiliser (self, cible) :
        cible.health -= self.attack_power*self.precision*(cible.defense/100)*1/self.distance_attack
        return cible.health
        
        

class Bloquer_adversaire (Unit):
    def __init__(self):
        self.name = "Bloquer_adversaire"
        self.offsets = [
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)   # Diagonales proches
                ]
        self.temps = 3
        self.attack_power = 40
        self.quantite = 2
        self.distance_attack = 4
        self.precision = random.uniform(0.5, 1)        

class Attaque_toile (Unit):
    def __init__(self):
        self.name = "Attaque_toile"
        self.offsets = [
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonales proches
                ]
        self.attack_power = 50
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

class Marteau (Unit):
    def __init__(self):
        self.name = "Marteau"
        self.offsets = [
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 130
        self.quantite = 2
        self.distance_attack = 5
        self.precision = random.uniform(0.5, 1)
        
class Foudre (Unit):
    def __init__(self):
        self.name = "Foudre"
        self.offsets = [
                (-6, 0), (6, 0), (0, -6), (0, 6),
                (-5, 0), (5, 0), (0, -5), (0, 5),
                (-4, 0), (4, 0), (0, -4), (0, 4),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, 0), (2, 0), (0, -2), (0, 2),
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
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 40
        self.quantite = 100
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)

class Protection (Unit):
    def __init__(self):
        self.name = "Protection"
        self.offsets = [
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
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
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonales proches
                ]
        self.attack_power = 120
        self.quantite = 10
        self.distance_attack = 4
        self.precision = random.uniform(0.5, 1)

class Fleche_yaka(Unit) :
    def __init__(self):
        self.name = "Fleche_Yaka"
        self.offsets = [
                (-3,-3), (-3, 3), (3, -3), (3, 3),
                (-3,-2), (-3, 2), (3, -2), (3, 2),
                (-3, -1), (-3, 1), (3, -1), (3, 1),
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1) ,  # Diagonales proches
                ]
        self.attack_power = 100
        self.quantite = 3
        self.distance_attack = 1
        self.precision = random.uniform(0.5, 1)

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
                (-3, 0), (3, 0), (0, -3), (0, 3),
                (-2, -2), (-2, 2), (2, -2), (2, 2),
                (-2, 0), (2, 0), (0, -2), (0, 2),
                (-2, 1), (2, 1), (1, -2), (1, 2),
                (-1, 0), (1, 0), (0, -1), (0, 1),  # Orthogonaux : gauche, droite, haut, bas
                (-1, -1), (1, 1), (-1, 1), (1, -1)  # Diagonales proches
                ]
        self.attack_power = 100
        self.quantite = 3
        self.distance_attack = 3
        self.precision = random.uniform(0.5, 1)
#hero = Unit("Captain_America",0,0,[55,55])
#mechant = Unit("Hulk",0,0,[55,55])
#hero.attack("Poings", mechant)



