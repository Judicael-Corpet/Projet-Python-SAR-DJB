import pygame 
import random
import pytmx
import pyscroll
import pygame
from moviepy import VideoFileClip

from unit import *
from menu import *
from sound import *


fond = pygame.image.load('Fond_ecran.png')

class Game:
    
    
    def __init__(self, screen):
        
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1220, 700
        self.display = pygame.Surface((self.DISPLAY_W ,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W ,self.DISPLAY_H)))
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

         # Mode de jeu
        self.Mode = Mode(self)
        self.Mode_jeu = Mode(self)

        self.attaque_selectionne = Aucune_action()
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        self.menu_attaques = False
        self.selected_attack = False
        self.list_enemy_health = []
        self.list_player_health = []
        self.player_units = []
        self.enemy_units = []
        self.is_selected = False
        
    
    def draw_attack_menu(self) :
        """Dessine le menu des attaques."""
        #Fond noir dans le coin inférieur gauche
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 530, 250, 150 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 530, 250, 150), 2)  # Bordure blanche

    

        list_attacks = self.attaques
        # Dessiner chaque attaque dans le rectangle
        for i, attaque in enumerate(list_attacks):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Mettre en surbrillance l'attaque sélectionnée
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 550 + i * 30))  # Positionnement des attaques

    def cases_teleportation(self, screen):
        self.cases_tp = [(4, 6), (3, 16), (27, 11)]  # Liste des cases de téléportation

        for player in self.player_units + self.enemy_units:  # Parcours des joueurs et ennemis
            for i in range(0, len(self.cases_tp)):  # On parcourt les indices valides de la liste des cases de téléportation
                if (player.x, player.y) == self.cases_tp[i]:
                    # Sélectionner une case d'arrivée différente de la case actuelle
                    available_cases = [0, 1, 2]  # Indices des cases de téléportation
                    available_cases.remove(i)  # Enlever l'indice de la case actuelle

                    # Choisir une case d'arrivée parmi les indices restants
                    r = random.choice(available_cases)
                    (self.arrivex,self.arrivey) = self.cases_tp[r]  # Sélection de la case d'arrivée
                    player.x, player.y = (self.arrivex+1,self.arrivey+1)  # Mise à jour des coordonnées du joueur
                    break  # On quitte la boucle dès qu'une téléportation est effectuée
                    
                
                
    def cases_soin(self, screen):
     
        self.case_soin=[[23,10],[24,10],[24,11],[23,11],[7,17],[8,17],[7,18],[8,18]]
        color = WHITE
        color1=(20,255,20)
        half_size = CELL_SIZE // 2  # La moitié de la taille d'une cellule
        line_width = 15  # Épaisseur des lignes de la croix
      
        for i, player in enumerate(self.player_units):
            for j in range(0,len(self.case_soin)):
                if player.x==self.case_soin[j][0] and player.y== self.case_soin[j][1]:
                    hero_selected = player.attribuer_class_perso()
                    self.list_player_health[i] = hero_selected.health_max
                    print (f"{hero_selected.name} a été soigné")
        return self.list_player_health


    def cases_degat(self, screen):
        self.case_degat = [[13,15],[14,15],[15,15],[16,15],[17,15],[18,15],[19,13],[20,13],[21,13],[22,13],[23,13],[24,13]]
       
        degat = 5
        
        for i, player in enumerate(self.player_units) :
            for j in range(0,len(self.case_degat)):
                if player.x==self.case_degat[j][0] and player.y== self.case_degat[j][1]:
                    player_health = self.list_player_health[i]
                    player_health -= degat
                    print(player_health)
                    print("joueur a été blaissé sur le champ de mines")
                    self.list_player_health[i] = player_health
        
        for i, enemy in enumerate(self.enemy_units) :
            for j in range(0,len(self.case_degat)):
                if enemy.x==self.case_degat[j][0] and enemy.y== self.case_degat[j][1]:
                    enemy_health = self.list_enemy_health[i]
                    enemy_health -= degat
                    print(enemy_health)
                    print("l'enemi a été blaissé sur le champ de mines")
                    self.list_enemy_health[i] = enemy_health
        
        return self.list_enemy_health
                  

    def handle_player_turn(self):
        """Tour du joueur"""
        print ("DEBUT DU TOUR DU JOUEUR")

        for selected_unit in self.player_units:
            selected_unit.is_selected = True
            has_acted = False            
            selected_unit.update_green_case(self.player_units, self.enemy_units)
            hero_selected = selected_unit.attribuer_class_perso()
            health = hero_selected.get_health()
            self.selected_attack_index = 0
            nbre_move = hero_selected.nbre_move
            defense = hero_selected.defense
            print (f"l'unité est : {selected_unit.name}")
            print(f"Points de vie :{health}, nbre_move = {nbre_move}, defense = {defense}")
            self.flip_display()
            
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
                                self.attaques = hero_selected.list_attaques
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
                                self.selected_attack = True
                                self.menu_attaques = False
                                attaque_selectionne = hero_selected.attribuer_class_attaque(self.selected_attack_index)

                                for i, enemy in enumerate (self.enemy_units) :
                                    enemy_selected = enemy.attribuer_class_perso() 
                                    enemy_health = self.list_enemy_health[i]                           
                                    new_enemy_health = selected_unit.attack(attaque_selectionne, enemy_selected, enemy_health)
                                    self.list_enemy_health[i] = new_enemy_health

                                    if enemy_health <= 0 :
                                        print(f"{enemy.name} est mort") 
                                        self.enemy_units.remove(enemy)
                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                    self.flip_display()   

        return self.list_enemy_health
                            
                
    def handle_player_2_turn(self):
        """Tour du joueur"""
        print ("DEBUT DU TOUR DU JOUEUR")
        for selected_unit in self.enemy_units:
            selected_unit.is_selected = True
            has_acted = False
            
    
            selected_unit.update_green_case(self.enemy_units, self.player_units)
            hero_selected = selected_unit.attribuer_class_perso()
            #health = hero_selected.get_health()
            self.selected_attack_index = 0
            self.flip_display()
            
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
                                self.attaques = hero_selected.list_attaques
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
                                self.selected_attack = True
                                self.menu_attaques = False
                                attaque_selectionne = hero_selected.attribuer_class_attaque(self.selected_attack_index)
                                
                                for i, player in enumerate (self.player_units) :
                                    player_selected = player.attribuer_class_perso()  
                                    player_health = self.list_player_health[i]    
                                    new_player_health = selected_unit.attack(attaque_selectionne, player_selected, player_health)
                                    self.list_player_health[i] = new_player_health

                                    if player_health <= 0 :
                                        print(f"{player.name} est mort") 
                                        self.player_units.remove(player)
                                
                                has_acted = True
                                selected_unit.is_selected = False 
                
                    self.flip_display()   

        return self.list_player_health

    def handle_enemy_turn(self):
        """IA très simple pour les ennemis."""
        print ("DEBUT DU TOUR DE L'ENNEMI")
        
        for enemy in self.enemy_units:
            
            enemy_selected = enemy.attribuer_class_perso()
            print(f"LENNEMI CHOISI EST {enemy_selected.name}")
            
            enemy.is_selected  = True 
            enemy.update_green_case(self.player_units,self.enemy_units)   
            #Choix d'une cible au hasard    
            target = random.choice(self.player_units)
            i = self.player_units.index(target) 
            print (f"indice pour le choix du joueur ciblé est i = {i}")
            # Déplacement vers la cible
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)
          
            
            # Attaque si possible
            
            player_selected = target.attribuer_class_perso() 
            #choix d'une attaque
            if abs(enemy.x - player_selected.x) <= enemy.distance_maxi_attack and abs(enemy.y - player_selected.y) <= enemy.distance_maxi_attack :
                enemy_attack = random.choice(enemy_selected.list_attaques[1:])
                indice = enemy_selected.list_attaques.index(enemy_attack)
                print (f"indice pour l'attaque enemy est {indice}" )
                enemy_attack_selected = enemy_selected.attribuer_class_attaque(indice) 
                print (f"l'attaque enemy est {enemy_attack_selected.name}")
                player_health = self.list_player_health[i]
                print (f"MA VIE NE TIENT QU'A {player_health}")
                new_player_health = enemy_selected.eni_attack(enemy_attack_selected, player_selected, player_health)
                self.list_player_health[i] = new_player_health
                print (f"QUE TREPAS SI JE FAIS BLI {new_player_health}")
            else :
                enemy_attack_selected = Aucune_action()
                print("J'ai choisi de ne pas attaquer")

                player_health = self.list_player_health[i]

            if player_health <= 0:
                print(f"{target.name} est mort")
                self.player_units.remove(target)
            
            self.flip_display()

            enemy.is_selected = False
            pygame.time.wait(1000)
        play = True
        return play, self.list_player_health

    def flip_display(self):
        """Affiche la carte et les éléments du jeu."""
        # Chargement des données de la carte
        tmx_data = pytmx.util_pygame.load_pygame('map_cyber.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        
        # Rendu de la carte
        map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1  # Ajustez si nécessaire
        
        # Groupe Pyscroll pour les sprites et la carte
        self.group = pyscroll.PyscrollGroup(map_layer = map_layer, default_layer=5)
       
        # Dessinez la carte
        self.group.update()
        self.group.draw(self.screen)
        
        #dessine logo
        logo_marvel=pygame.image.load('Marvel_Logo.svg.png')
        logo_marvel=pygame.transform.scale(logo_marvel,(32*9,32*3))
        self.screen.blit(logo_marvel,(32*4,12))

        # Dessine le texte
        porte=pygame.image.load('porte.png')
        porte=pygame.transform.scale(porte,(32,32))
        self.screen.blit(porte,(32*25 + 10,32*18 + 10))
        teleport=pygame.image.load('texte_case_teleportation.png')
        teleport=pygame.transform.scale(teleport,(32*6,32))
        self.screen.blit(teleport,(32*26 + 10,32*18 + 10))

        soin=pygame.image.load('Soin.png')
        soin=pygame.transform.scale(soin,(32,32))
        self.screen.blit(soin,(32*25 + 10,32*19 + 10))
        soin_texte=pygame.image.load('texte_case_soin.png')
        soin_texte=pygame.transform.scale(soin_texte,(32*3,32))
        self.screen.blit(soin_texte,(32*26 + 10,32*19 + 10))

        degat=pygame.image.load('degat.png')
        degat=pygame.transform.scale(degat,(32,32))
        self.screen.blit(degat,(32*25 + 10, 32*20 + 10))
        degat_texte=pygame.image.load('texte_case_degat.png')
        degat_texte=pygame.transform.scale(degat_texte,(32*4 - 15,32))
        self.screen.blit(degat_texte,(32*26 + 10,32*20 + 10))

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
                pygame.draw.rect(self.screen, WHITE, rect, -1)

        # Ajoutez les sprites des unités/players
        for i, perso in enumerate(self.enemy_units) :
            perso_selected = perso.attribuer_class_perso()
            health_perso = self.list_enemy_health[i]
            perso.draw(self.screen)
            perso_selected.draw_health_bar(self.screen, health_perso)

            if perso.is_selected :
                perso.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso.draw_red_case(self.screen, )

            
        for i, perso1 in enumerate(self.player_units):
            perso1_selected = perso1.attribuer_class_perso()
            health_perso1 = self.list_player_health[i]
            perso1.draw(self.screen)
            perso1_selected.draw_health_bar(self.screen, health_perso1)
            
            if perso1.is_selected :
                if self.menu_attaques == False :
                    perso1.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso1.draw_red_case(self.screen, )


         # Si le menu des attaques est actif, dessiner le menu par-dessus
        if self.menu_attaques:  
            self.draw_attack_menu()

        pygame.display.flip()


    def flip_display_ecran_final(self):
        """Affiche la carte et les éléments du jeu."""
        fond_fin = pygame.image.load('Fond_ecran.png')
        self.display.blit(fond_fin, (0, 0))

        if (len(self.enemy_units) == 0) and self.Mode_jeu :
            print("Tous les ennemis ont été éliminés !")
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
            
        elif (len(self.player_units) == 0) and self.Mode_jeu :
            print("Tous les players ont été éliminés !")
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)

        elif (len(self.enemy_units) == 0) and not(self.Mode_jeu) :
            print("Tous les players du joueur 2 ont été éliminés !")
            self.draw_text_black('Victoire J1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victoire J1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victoire J1 !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victoire J1 !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victoire J1 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
            
        elif (len(self.player_units) == 0) and not(self.Mode_jeu) :
            print("Tous les players du joueur 1 ont été éliminés !")
            self.draw_text_black('Victoire J2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victoire J2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victoire J2 !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victoire J2 !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victoire J2 !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
        self.window.blit(self.display, (0, 0)) 
        pygame.display.update()


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
    
    # Fonction pour afficher la vidéo
    def play_video(self,clip):
        clock = pygame.time.Clock()
        for frame in clip.iter_frames(fps=30, dtype="uint8"):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
            # Convertir l'image pour Pygame et l'afficher
            pygame_frame = pygame.surfarray.make_surface(frame.swapaxes(0, 1))
            self.screen.blit(pygame_frame, (0, 0))
            pygame.display.update()
            clock.tick(30)

def main():

    
    
    # Initialisation de Pygame
    pygame.init()
    
    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("Marvel Game")
    
    # Instanciation du jeu
    game = Game(screen)
    
    clip = VideoFileClip("intro_video.mp4")
    game.play_video(clip)
    
    while game.running:
        game.curr_menu.display_menu()
        if (game.playing):
            break
                     
    player1 = Unit(game.Choix_Personnages_1.game_personnage, 15, 10, [32,32], game)
    hero1 = player1.attribuer_class_perso()
    hero_health1 = hero1.get_health()
    game.player_units.append(player1)
    game.list_player_health.append(hero_health1)
    player2 = Unit(game.Choix_Personnages_2.game_personnage, 15, 12, [32,32], game)
    hero2 = player2.attribuer_class_perso()
    hero_health2 = hero2.get_health() 
    game.player_units.append(player2)
    game.list_player_health.append(hero_health2) 
        
    print (f"NBRE DE POINTS DE VIE DE {player1.name} = {hero_health1}")
    print (f"NBRE DE POINTS DE VIE DE {player2.name} = {hero_health2}")


    #game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 0, 9, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             #Unit(game.Choix_Personnages_4.game_personnage, 1, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]

    player3 = Unit(game.Choix_Personnages_3.game_personnage, 22, 19, [32,32], game)
    hero3 = player3.attribuer_class_perso()
    hero_health3 = hero3.get_health()
    game.enemy_units.append(player3)
    game.list_enemy_health.append(hero_health3)
    player4 = Unit(game.Choix_Personnages_4.game_personnage, 23, 19, [32,32], game)
    hero4 = player4.attribuer_class_perso()
    hero_health4 = hero4.get_health()
    game.enemy_units.append(player4)
    game.list_enemy_health.append(hero_health4)

    print (f"NBRE DE POINTS DE VIE DE {player3.name} = {hero_health3}")
    print (f"NBRE DE POINTS DE VIE DE {player4.name} = {hero_health4}")

    print(f"liste des joueurs : {game.player_units}")
    print(f"liste des points de vie des joueurs : {game.list_player_health}")
    print(f"liste des ennemis : {game.enemy_units}")
    print(f"liste des points de vie des enemy : {game.list_enemy_health}")

    play = True
    iter = 0
    
    # Boucle principale du jeu
    while play and iter<100 :
        game.handle_player_turn()
        if (len(game.enemy_units) == 0) :
            game.flip_display_ecran_final()
            pygame.time.wait(5000)
            play = False
        if game.Mode_jeu :
            game.handle_enemy_turn()  
            if (len(game.player_units) == 0) :
                game.flip_display_ecran_final()
                pygame.time.wait(5000)
                play = False
        else :
            game.handle_player_2_turn()
            if (len(game.player_units) == 0) :
                game.flip_display_ecran_final()
                pygame.time.wait(5000)
                play = False
        iter += 1
        if (len(game.player_units) != 0) and (len(game.enemy_units) != 0) :
            game.flip_display()
    return game.list_player_health, game.list_enemy_health 


if __name__ == "__main__":
    main()