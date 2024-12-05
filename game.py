import pygame 
import random
import pytmx
import pyscroll
import numpy as np
from unit import *
from menu import *
from sound import *
from IA import *
import heapq

fond = pygame.image.load('Fond_ecran.png')

personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Groot", "Wolverine", "Black_Panther", 
                            "Starlord", "Yondu", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]
"""
grid = [
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0],
    [0, 0, 2, 2, 2, 2, 1, 0, 2, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1],
    [0, 0, 0, 1, 0, 2, 2, 2, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [1, 1, 1, 0, 0, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 2, 0, 0, 0, 0, 1, 1, 1, 0, 2, 2, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1, 1],
]
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
        self.Choix_Carte = Choix_Carte_Menu(self)
        self.curr_menu = self.main_menu

        # gerer le son
        self.sound_manager = SoundManager()
        self.Volume = Volume(self)
        self.Musique = Volume(self)

        
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]
        self.menu_attaques = False
        self.selected_attack = False

        self.player_units = []
        self.enemy_units = []
        #p1 = Unit("Captain_America", 0, 0, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"])
        #print (p1.name)
        

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
         
        
        for selected_unit in self.player_units:
            self.flip_display()
            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            selected_unit.is_selected = True
            selected_unit.update_green_case(self.player_units,self.enemy_units)
            list_attacks = selected_unit.attaques
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
                                #selected_unit.update_sprite("left")
                                dx = -1
                            elif event.key == pygame.K_RIGHT:
                                #selected_unit.update_sprite("right")
                                dx = 1
                            elif event.key == pygame.K_UP and not self.menu_attaques:
                                #selected_unit.update_sprite("up")
                                dy = -1
                            elif event.key == pygame.K_DOWN and not self.menu_attaques:
                                #selected_unit.update_sprite("down")
                                dy = 1
                            selected_unit.move(dx, dy)
                            
                        

                        # Attaque (touche espace) met fin au tour
                            if event.key == pygame.K_SPACE:
                                self.attaques = selected_unit.attaques
                                self.menu_attaques = True #active le menu des attaques
                            # Navigation dans le menu des attaques
                        if self.menu_attaques :
                            if event.key == pygame.K_DOWN:
                                self.selected_attack_index = (self.selected_attack_index + 1) % len(self.attaques) # Navigation dans le menu des attaques vers le haut
                            
                            elif event.key == pygame.K_UP:
                                self.selected_attack_index = (self.selected_attack_index - 1) % len(self.attaques) # Navigation dans le menu des attaques vers le bas
                            
                            elif event.key == pygame.K_RETURN :
                                print (f"Attaque sélectionnée : {self.attaques[self.selected_attack_index]}") # attaque validée
                                self.selected_attack = True
                                self.menu_attaques = False
                                #screen.fill((0, 0, 128))  # Efface l'écran (fond bleu foncé)
                                

                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                           #selected_unit.update_green_case(self.player_units, self.enemy_units)
                    self.flip_display()   
               
#Suite du code à écrire ici pour pour appliquer l'attaque à l'ennemi ciblé
                        
                        #if self.selected_attack :
                                
            
                                  
                
                

                            #print(f"Attaque choisie : {attack['name']}")
                            #for enemy in self.enemy_units:
                            #    if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                            #        selected_unit.attack(enemy)
                            #        if enemy.health <= 0:
                            #            self.enemy_units.remove(enemy)

                            
                
    



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
            target_x_1 = self.player_units[0].x
            target_y_1 = self.player_units[0].y
            target_vie_1 = self.player_units[0].health
            target_x_2 = self.player_units[1].x
            target_y_2 = self.player_units[1].y
            target_vie_2 = self.player_units[1].health
            # DEPLACEMENT
            #if np.sqrt((target_x_1 - enemy.x)**2+(target_y_1 - enemy.y)**2) < np.sqrt((target_x_2 - enemy.x)**2+(target_y_2 - enemy.y)**2) :
            #    target_x = self.player_units[0].x
            #    target_y = self.player_units[0].y
            #    dx = 1 if enemy.x < target_x else -1 if enemy.x > target_x else 0
            #    dy = 1 if enemy.y < target_y else -1 if enemy.y > target_y else 0
            #    enemy.move(dx, dy)

                # ATTAQUE
                #if np.sqrt((target_x_1 - enemy.x)**2+(target_y_1 - enemy.y)**2) == np.sqrt((target_x_2 - enemy.x)**2+(target_y_2 - enemy.y)**2) :
                #    if target_vie_1 < target_vie_2 :
                #
                #         pass #attaquer le 1


            #if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
            #    enemy.attack(target)
            #    if target.health <= 0:
            #        self.player_units.remove(target)
        

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
        
        # Ajout dune grille
        for x in range(0, WIDTH, CELL_SIZE):
            for y in range(0, HEIGHT, CELL_SIZE):
                rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

        # Ajoutez les sprites des unités/players
        for unit in self.player_units + self.enemy_units :
            unit.draw(self.screen)
            if unit.is_selected :
                unit.draw_green_case(self.screen)
            
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
    pygame.display.set_caption("Mon jeu de stratégie")
    
    # Instanciation du jeu
    game = Game(screen)

    while game.running:
        game.curr_menu.display_menu()
        if (game.playing):
            break
    
    game.player_units = [Unit(game.Choix_Personnages_1.game_personnage, 0, 0, [55,55]),#,150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_2.game_personnage, 0, 1, [55,55])]#, 150 , 3, 75, ["Poings", "Lancer_bouclier"] )]                  

    game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 5, 5, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_4.game_personnage, 16, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]
    
    play = True
    iter = 0
    
    # Boucle principale du jeu
    while play and iter<100 :
        game.handle_player_turn()
        game.handle_enemy_turn()   
        iter += 1 
        play =  game.handle_enemy_turn() 

if __name__ == "__main__":
    main()