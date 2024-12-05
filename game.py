import pygame 
import random
import pytmx
import pyscroll
import numpy as np
import heapq
from unit import *
from menu import *
from sound import *


fond = pygame.image.load('Fond_ecran.png')

#personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Groot", "Wolverine", "Black_Panther", 
                            #"Starlord", "Yondu", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]
"""
grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]"""
grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
]

#passer d'un côté si on est de ce coté de la colonne sinon de l'autre

def a_star_with_memory(grid, start, goal):
    def heuristic(a, b):
        """Distance de Manhattan pour estimer le coût restant."""
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(grid), len(grid[0])
    open_set = []  # File de priorité
    heapq.heappush(open_set, (0, start))  # Ajoute la case de départ avec un score f=0
    came_from = {}  # Garde une trace des déplacements
    g_score = {start: 0}  # Coût pour atteindre un nœud
    f_score = {start: heuristic(start, goal)}  # Score total estimé (g + h)
    closed_set = set()  # Garde une trace des nœuds déjà explorés

    while open_set:
        _, current = heapq.heappop(open_set)  # Récupère le nœud avec le plus faible f_score

        # Si on atteint l'objectif
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)  # Inclut le point de départ
            path.reverse()  # Retourne le chemin
            return path  # Retourne le chemin trouvé

        closed_set.add(current)  # Marque comme exploré

        # Explore les voisins (haut, bas, gauche, droite)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Vérifie si le voisin est dans la grille et accessible
            if (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and 
                grid[neighbor[0]][neighbor[1]] != 1 and neighbor not in closed_set):

                tentative_g_score = g_score[current] + 1  # Coût d'un pas supplémentaire

                # Si le coût pour atteindre ce voisin est meilleur, on met à jour
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                    # Ajouter à l'open_set si pas déjà présent
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Aucun chemin trouvé




class Game:
    """
    Classe pour représenter le jeu.

    ...
    Attributs
    ---------
    screen: pygame.Surface 
        La surface de la fenêtre du jeu.
    player_units : list[Unit]
        La liste des unités du joueur.
    enemy_units : list[Unit]
        La liste des unités de l'adversaire.
    """
    
    def __init__(self, screen):
        """
        Construit le jeu avec la surface de la fenêtre.
        Paramètres
        ----------
        screen : pygame.Surface
            La surface de la fenêtre du jeu.
        """
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1080, 720
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = '8-BIT WONDER.TTF'
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)


        self.main_menu = MainMenu(self) # instanciation de self.main_menu à la classe MainMenu dans menu.py
        self.options = OptionsMenu(self) #instanciation de self.options à la classe OptionsMenu dans menu.py
        self.credits = CreditsMenu(self) #instanciation de self.credits à la classe CreditsMenu dans menu.py
        
        
        self.Choix_Personnages_1 = Choix_Personnage_Menu_1(self) #Instanciation de self.Choix_Personnages_1 à la classe Choix_Personnage_Menu_1 dans menu.py
        self.Choix_Personnages_2 = Choix_Personnage_Menu_2(self) #Instanciation de self.Choix_Personnages_2 à la classe Choix_Personnage_Menu_2 dans menu.py
        self.Choix_Personnages_3 = Choix_Personnage_Menu_3(self) #Instanciation de self.Choix_Personnages_3 à la classe Choix_Personnage_Menu_3 dans menu.py
        self.Choix_Personnages_4 = Choix_Personnage_Menu_4(self) #Instanciation de self.Choix_Personnages_4 à la classe Choix_Personnage_Menu_4 dans menu.py
        # self.Choix_Carte = Choix_Carte_Menu(self)
        self.curr_menu = self.main_menu

        # gerer le son
        self.sound_manager = SoundManager()
        self.Volume = Volume(self)
        self.Musique = Volume(self)

        
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        #self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]
        self.menu_attaques = False
        self.selected_attack = False

        self.player_units = []
        self.enemy_units = []
        #p1 = Unit("Captain_America", 0, 0, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"])
        #print (p1.name)
    
        self.cases=[]
        self.case_tp=[]
    
    def cases_teleportation(self,screen):
        self.cases_tp=[3,3]
        cas_arrive=[15,10]
        color=(255, 255, 100)
        pygame.draw.rect(screen, color, (self.cases_tp[0]*CELL_SIZE, self.cases_tp[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Dessine les bords
        # pygame
        for player in self.player_units:
            if player.x==self.cases_tp[0] and player.y== self.cases_tp[1]:
                player.x,player.y=(cas_arrive[0],cas_arrive[1])
                
    def cases_soin(self, screen):
        self.case_soin = [5, 3] 
        color = WHITE
        color1=(20,255,20)
        x, y = self.case_soin  # Position de la case
        half_size = CELL_SIZE // 2  # La moitié de la taille d'une cellule
        line_width = 15  # Épaisseur des lignes de la croix
        bonus_health=30
        for player in self.player_units:
            if player.x==self.case_soin[0] and player.y== self.case_soin[1]:
            
                if player.health<=120:
                    player.health+=bonus_health
                    print("joueur a été soigné")
                elif player.health>120:
                    print("joueur a été soigné")
                    player.health=150
                

        # dessine le fond:
        pygame.draw.rect(screen, color1, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Dessine les bords

        # Dessiner la ligne verticale
        pygame.draw.line(
            screen, 
            color, 
            (x * CELL_SIZE + half_size , y * CELL_SIZE+5),  # Début de la ligne
            (x * CELL_SIZE + half_size , y * CELL_SIZE + CELL_SIZE-5),  # Fin de la ligne
            line_width  # Épaisseur
        )

        # Dessiner la ligne horizontale
        pygame.draw.line(
            screen, 
            color, 
            (x * CELL_SIZE+5, y * CELL_SIZE + half_size ),  # Début de la ligne
            (x * CELL_SIZE + CELL_SIZE-5, y * CELL_SIZE + half_size ),  # Fin de la ligne
            line_width  # Épaisseur
        )
        
        

            
    def cases_degat(self, screen):
        self.case_degat = [1, 1]
        color = BLACK
        color1=(255,20,20)
        x, y = self.case_degat  # Position de la case
        half_size = CELL_SIZE // 2  # La moitié de la taille d'une cellule
        line_width1 = 10  # Épaisseur des lignes de verticales
        line_width2=5 # épaisseur horizontale 

        degat=1600
        
        for player in self.player_units:
            if player.x==self.case_degat[0] and player.y== self.case_degat[1]:
                player.health-=degat
                print(player.health)
                print("joueur a été blaissé")
                  
                
        # dessine le fond:
        pygame.draw.rect(screen, color1, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE))  # Dessine les bords

        # Dessiner la ligne verticale
        pygame.draw.line(
            screen, 
            color, 
            (x * CELL_SIZE + half_size , y * CELL_SIZE+5),  # Début de la ligne
            (x * CELL_SIZE + half_size , y * CELL_SIZE + CELL_SIZE-5),  # Fin de la ligne
            line_width1  # Épaisseur
        )

        # Dessiner la ligne horizontale
        pygame.draw.line(
            screen, 
            color, 
            (x * CELL_SIZE+10, y * CELL_SIZE + 35 ),  # Début de la ligne
            (x * CELL_SIZE + CELL_SIZE-10, y * CELL_SIZE + 35),  # Fin de la ligne
            line_width2  # Épaisseur
        )
        
    
    def draw_attack_menu(self) :
        """Dessine le menu des attaques."""
        #Fond noir dans le coin inférieur gauche
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 340, 250, 150 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 340, 250, 150), 2)  # Bordure blanche

        #if selected_unit == "Captain_America" :
        #self.attaques = []
        #self.attaques = ["Aucune_action", "Poings", "Lancer_bouclier"]
        list_attacks = self.attaques
        # Dessiner chaque attaque dans le rectangle
        for i, attaque in enumerate(list_attacks):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Mettre en surbrillance l'attaque sélectionnée
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 350 + i * 30))  # Positionnement des attaques
            

    def handle_player_turn(self):
        """Tour du joueur"""
        new_health = 0 
        
        for selected_unit in self.player_units:
           
            #self.flip_display()
            
            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            selected_unit.is_selected = True
            selected_unit.update_green_case(self.player_units,self.enemy_units)
            self.selected_attack_index = 0
            #selected_attack = Aucune_action()
            
            health = selected_unit.health
            nbre_move = selected_unit.nbre_move
            defense = selected_unit.defense
            print (f"l'unité est : {selected_unit.name}, {selected_unit.defense}")
            print(f"Points de vie :{health}, nbre_move = {nbre_move}, defense = {defense}")
            #self.flip_display()
            
            while not has_acted:
                
                # Important: cette boucle permet de gérer les événements Pygame
                for event in pygame.event.get():

                    # Gestion de la fermeture de la fenêtre
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()

                    # Gestion des touches du clavier
                    elif event.type == pygame.KEYDOWN:
                        if self.menu_attaques == False :
                        # Déplacement (touches fléchées)
                            dx, dy = 0, 0
                            if event.key == pygame.K_LEFT:
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                dx = 1
                            elif event.key == pygame.K_UP and not self.menu_attaques:
                                dy = -1
                                
                            elif event.key == pygame.K_DOWN and not self.menu_attaques:
                                dy = 1
                                
                            selected_unit.move(dx, dy)
                            
                        

                        # Attaque (touche espace) met fin au tour
                            if event.key == pygame.K_SPACE:
                                self.attaques = selected_unit.attaques
                                self.menu_attaques = True #active le menu des attaques
                            # Navigation dans le menu des attaques
                        if self.menu_attaques :
                            selected_unit.update_red_case(self.attaques[self.selected_attack_index])

                            if event.key == pygame.K_DOWN:
                                self.selected_attack_index = (self.selected_attack_index + 1) % len(self.attaques) # Navigation dans le menu des attaques vers le haut
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])
                            elif event.key == pygame.K_UP:
                                self.selected_attack_index = (self.selected_attack_index - 1) % len(self.attaques) # Navigation dans le menu des attaques vers le bas
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])
                            elif event.key == pygame.K_RETURN :
                                print("MMMMMMMMMMMMM")
                                print (f"Attaque sélectionnée : {self.attaques[self.selected_attack_index]}") # attaque validée
                                self.selected_attack = True
                                
                                self.menu_attaques = False
                                #screen.fill((0, 0, 128))  # Efface l'écran (fond bleu foncé)
                                
                                
                                
                                for i, enemy in enumerate (self.enemy_units) :                                  
                                    selected_unit.attack(self.attaques[self.selected_attack_index], enemy)
                                    
                                    print (enemy.health)
                                        
                                    if enemy.health <= 0 :
                                        print(f"{enemy.name} est mort") 
                                        self.enemy_units.remove(enemy)
                                    
                                for player in self.player_units:
                                    player.update_health_bar()
                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                    # self.flip_display()   

                    
                    # for unit in self.player_units:
                    #     if unit.health <= 0:
                    #         self.player_units.remove(unit)
                    
                    self.flip_display()

                            
    """            
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
                
                current_grid[unit.y][unit.x] = 1  # Marquer les cases occupées comme obstacles

            # Appliquer A* pour trouver le chemin vers la cible
            start = (enemy.x, enemy.y)
            goal = (target.x, target.y)

            path = a_star_with_memory(current_grid, start, goal)
            print(f"Path found: {path}")
            
            if path and len(path) > 1:
                next_step = path[0]  # Le prochain pas après la position actuelle
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
                enemy.move(enemy.x, enemy.y)
            else:
                print("Aucun chemin trouvé pour l'ennemi :", enemy)

            # Si l'ennemi est à portée, attaquer
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

            enemy.is_selected = False

        self.flip_display()
        play = True
        return play


    """
    def handle_enemy_turn(self):
        #IA très simple pour les ennemis.
       
        
        for enemy in self.enemy_units:
            enemy.is_selected  = True 
             
            enemy.update_green_case(self.player_units,self.enemy_units)   

                # Déplacement aléatoire
            target_x_1 = self.player_units[0].x
            target_y_1 = self.player_units[0].y
            target_vie_1 = self.player_units[0].health
            target_x_2 = self.player_units[1].x
            target_y_2 = self.player_units[1].y
            target_vie_2 = self.player_units[1].health
            if np.sqrt((target_x_1 - enemy.x)**2+(target_y_1 - enemy.y)**2) < np.sqrt((target_x_2 - enemy.x)**2+(target_y_2 - enemy.y)**2) :
                target_x = self.player_units[0].x
                target_y = self.player_units[0].y
                dx = 1 if enemy.x < target_x else -1 if enemy.x > target_x else 0
                dy = 1 if enemy.y < target_y else -1 if enemy.y > target_y else 0
                enemy.move(dx, dy)

            enemy_attack = random.choice(enemy.attaques)

            # Attaque si possible
            for player in self.player_units :
                new_player_health = enemy.attack(enemy_attack,player)
                player.health = new_player_health
                print(player.health)
                    
                if player.health <= 0:
                    #index = self.player_units.index(player)
                    #self.player_units = self.player_units.pop(index)
                    print(f"{player.name} est mort")
                    self.player_units.remove(player)
            enemy.is_selected = False
        #self.flip_display() 
        play = True
        return play 
    



    def flip_display(self):
        """Affiche la carte et les éléments du jeu."""
        # Chargement des données de la carte
        tmx_data = pytmx.util_pygame.load_pygame('map/map.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        
        # Rendu de la carte
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1  # Ajustez si nécessaire
        
        # Groupe Pyscroll pour les sprites et la carte
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=5)
       
        # Dessinez la carte
        self.group.update()
        self.group.draw(self.screen) 
        # Dessine cases de téléportations
        self.cases_teleportation(self.screen)
        # Dessine cases soins
        self.cases_soin(self.screen)
        #Dessine cases degats
        self.cases_degat(self.screen)
        
        # Ajout dune grille
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        # Ajoutez les sprites des unités/players
        for perso in self.enemy_units:
            perso.draw(self.screen)
            perso.draw_health_bar(self.screen)
            
        for perso1 in self.player_units:
            perso1.draw(self.screen)
            perso1.draw_health_bar(self.screen)
            if perso1.is_selected :
                perso1.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso1.draw_red_case(self.screen)


         # Si le menu des attaques est actif, dessiner le menu par-dessus
        if self.menu_attaques:  
            self.draw_attack_menu()
   
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text_white(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def draw_text_black(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
    

def main():

    # Initialisation de Pygame
    pygame.init()
    
    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Marvel Game")
    
    # Instanciation du jeu
    game = Game(screen)

    while game.running:
        game.curr_menu.display_menu()
        if (game.playing):
            break
    
    
    game.player_units = [Unit(game.Choix_Personnages_1.game_personnage, 0, 0, [55,55]),#,150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_2.game_personnage, 0, 1, [55,55])]#, 150 , 3, 75, ["Poings", "Lancer_bouclier"] )]                  

    
    game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 16, 9, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_4.game_personnage, 5, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]

    play = True
    iter = 0
    
    # Boucle principale du jeu
    while play and iter<100 :
        game.handle_player_turn()
        game.handle_enemy_turn()   
        
        iter += 1 
         

if __name__ == "__main__":
    main()