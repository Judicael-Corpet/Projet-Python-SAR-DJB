
import pygame 
import random
import pytmx
import pyscroll
from unit import *
from menu import *
from sound import *

fond = pygame.image.load('Fond_ecran.png')

#personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Groot", "Wolverine", "Black_Panther", 
                            #"Starlord", "Yondu", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]



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
<<<<<<< HEAD
        # self.Choix_Carte = Choix_Carte_Menu(self)
=======
        self.Choix_Carte = Choix_Carte_Menu(self)
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
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
        #self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]
        self.menu_attaques = False
        self.selected_attack = False
<<<<<<< HEAD

        self.player_units = []
        self.enemy_units = []
        #p1 = Unit("Captain_America", 0, 0, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"])
        #print (p1.name)
        

=======
        self.list_enemy_health = []
        self.list_player_health = []
        self.player_units = []
        self.enemy_units = []
        self.is_selected = False
        #p1 = Unit("Captain_America", 0, 0, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"])
        #print (p1.name)
        
    
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
    def draw_attack_menu(self) :
        """Dessine le menu des attaques."""
        #Fond noir dans le coin inférieur gauche
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 530, 250, 150 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 530, 250, 150), 2)  # Bordure blanche

<<<<<<< HEAD
        #if player == "Captain_America" :
        self.attaques = ["Aucune_action", "Poings", "Lancer_bouclier"]
        
=======
        #if selected_unit == "Captain_America" :
        #self.attaques = []
        #self.attaques = ["Aucune_action", "Poings", "Lancer_bouclier"]
        list_attacks = self.attaques
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
        # Dessiner chaque attaque dans le rectangle
        for i, attaque in enumerate(list_attacks):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Mettre en surbrillance l'attaque sélectionnée
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 550 + i * 30))  # Positionnement des attaques

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
        for i, player in enumerate(self.player_units):
            player_health = self.list_player_health[i]
            if player.x==self.case_degat[0] and player.y== self.case_degat[1]:
                player_health -= degat
                print(player.health)
                print("joueur a été blaissé")
            else :
                player_health = player_health
                  
            return player_health                    

    def handle_player_turn(self):
        """Tour du joueur"""
<<<<<<< HEAD

        
        for player in self.player_units:

            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            player.is_selected = True
            player.update_green_case(self.player_units,self.enemy_units)
            player.update_red_case()
            health = player.health
            nbre_move = player.nbre_move
            defense = player.defense
            print(f"Points de vie :{health}, nbre_move = {nbre_move}, defense = {defense}")
            # self.flip_display()
            
            while not has_acted:

=======
        print ("DEBUT DU TOUR DU JOUEUR")
        print(self.list_enemy_health)
        for selected_unit in self.player_units:
            selected_unit.is_selected = True
            has_acted = False
            #
            # selected_unit.draw_green_case(self.screen)
            
            selected_unit.update_green_case(self.player_units, self.enemy_units)
            print(selected_unit.green_cases)
            hero_selected = selected_unit.attribuer_class_perso()
            health = hero_selected.get_health()
        
            self.selected_attack_index = 0
            
            nbre_move = hero_selected.nbre_move
            defense = hero_selected.defense
            print (f"l'unité est : {selected_unit.name}")
            print(f"Points de vie :{health}, nbre_move = {nbre_move}, defense = {defense}")
            self.flip_display()
            
            while not has_acted:
                
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
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
                                
<<<<<<< HEAD
                            player.move(dx, dy)
=======
                            selected_unit.move(dx, dy)
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
                            
                        

                        # Attaque (touche espace) met fin au tour
                            if event.key == pygame.K_SPACE:
<<<<<<< HEAD
                                
                                self.menu_attaques = True #active le menu des attaques
                            # Navigation dans le menu des attaques
                        if self.menu_attaques :
                            player.update_red_case()
=======
                                self.attaques = hero_selected.list_attaques
                                self.menu_attaques = True #active le menu des attaques
                            # Navigation dans le menu des attaques
                        if self.menu_attaques :
                            selected_unit.update_red_case(self.attaques[self.selected_attack_index])

>>>>>>> efc26043aee740add8fd16090271b71780076ad3
                            if event.key == pygame.K_DOWN:
                                self.selected_attack_index = (self.selected_attack_index + 1) % len(self.attaques) # Navigation dans le menu des attaques vers le haut
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])
                            elif event.key == pygame.K_UP:
                                self.selected_attack_index = (self.selected_attack_index - 1) % len(self.attaques) # Navigation dans le menu des attaques vers le bas
                                selected_unit.update_red_case(self.attaques[self.selected_attack_index])
                            elif event.key == pygame.K_RETURN :
                                print("MMMMMMMMMMMMM")
                                print (f"index : {self.attaques[self.selected_attack_index]}") # attaque validée
                                self.selected_attack = True
                                
                                self.menu_attaques = False
                                #screen.fill((0, 0, 128))  # Efface l'écran (fond bleu foncé)
<<<<<<< HEAD

                                # for enemy in self.enemy_units:
                                #     if abs(player.x - enemy.x) <= 1 and abs(player.y - enemy.y) <= 1:
                                #         player.attack(enemy)
                                #         if enemy.health <= 0:
                                #             self.enemy_units.remove(enemy)

                                has_acted = True
                                player.is_selected = False 
                
                self.flip_display()
               
#Suite du code à écrire ici pour pour appliquer l'attaque à l'ennemi ciblé
                        
                        #if self.selected_attack :
                                
            
                                  
                
=======
                                
                                attaque_selectionne = hero_selected.attribuer_class_attaque(self.selected_attack_index)
                                print(attaque_selectionne.attack_power)
                                print(attaque_selectionne.precision)
                                print(attaque_selectionne.distance_attack)
                                

                                
                                for i, enemy in enumerate (self.enemy_units) :
                                    enemy_selected = enemy.attribuer_class_perso()
                                    print(enemy_selected.x, enemy_selected.y, enemy_selected.defense)  
                                    enemy_health = self.list_enemy_health[i]
                                    print (f"POUR L'INSTANT : {enemy_health}")
                                    print(attaque_selectionne.attack_power*attaque_selectionne.precision*(1 - enemy_selected.defense/100)/attaque_selectionne.distance_attack)                             
                                    new_enemy_health = selected_unit.attack(attaque_selectionne, enemy_selected, enemy_health)
                                                                        

                                    print (f"AILLLEE T'AS PRIS CHER!!!! IL TE RESTE {new_enemy_health} POINTS DE VIE !!!")
                                    self.list_enemy_health[i] = new_enemy_health

                                    if enemy_health <= 0 :
                                        print(f"{enemy.name} est mort") 
                                        self.enemy_units.remove(enemy)
                                
                                has_acted = True
                                selected_unit.is_selected = False 
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
                
                    self.flip_display()   

                            #print(f"Attaque choisie : {attack['name']}")
                            #for enemy in self.enemy_units:
                            #    if abs(player.x - enemy.x) <= 1 and abs(player.y - enemy.y) <= 1:
                            #        player.attack(enemy)
                            #        if enemy.health <= 0:
                            #            self.enemy_units.remove(enemy)
        return self.list_enemy_health
                            
                
    def handle_player_2_turn(self):
        """Tour du joueur"""
        print ("DEBUT DU TOUR DU JOUEUR")
        print(self.list_player_health)
        for selected_unit in self.enemy_units:
            selected_unit.is_selected = True
            has_acted = False
            #
            # selected_unit.draw_green_case(self.screen)
            
            selected_unit.update_green_case(self.enemy_units, self.player_units)
            print(selected_unit.green_cases)
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
                                print("MMMMMMMMMMMMM")
                                print (f"index : {self.attaques[self.selected_attack_index]}") # attaque validée
                                self.selected_attack = True

                                self.menu_attaques = False
                                #screen.fill((0, 0, 128))  # Efface l'écran (fond bleu foncé)
                                
                                attaque_selectionne = hero_selected.attribuer_class_attaque(self.selected_attack_index)
                                print(attaque_selectionne.attack_power)
                                print(attaque_selectionne.precision)
                                print(attaque_selectionne.distance_attack)
                                

                                
                                for i, player in enumerate (self.player_units) :
                                    player_selected = player.attribuer_class_perso()
                                    print(player_selected.x, player_selected.y, player_selected.defense)  
                                    player_health = self.list_player_health[i]
                                    print (f"POUR L'INSTANT : {player_health}")
                                    print(attaque_selectionne.attack_power*attaque_selectionne.precision*(1 - player_selected.defense/100)/attaque_selectionne.distance_attack)                             
                                    new_player_health = selected_unit.attack(attaque_selectionne, player_selected, player_health)
                                                                        

                                    print (f"AILLLEE T'AS PRIS CHER!!!! IL TE RESTE {new_player_health} POINTS DE VIE !!!")
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
<<<<<<< HEAD
       
        
        for enemy in self.enemy_units:
            enemy.is_selected  = True
            enemy.update_green_case(self.player_units,self.enemy_units)   

=======
        print ("DEBUT DU TOUR DE L'ENNEMI")
        
        for enemy in self.enemy_units:
            pygame.time.wait(1000)
            enemy_selected = enemy.attribuer_class_perso()
            enemy_health = enemy_selected.get_health()
            nbre_move = enemy_selected.nbre_move
            defense = enemy_selected.defense
            print (f"l'unité est : {enemy.name}, {enemy_selected.defense}")
            print(f"Points de vie :{enemy_health}, nbre_move = {nbre_move}, defense = {defense}")
            
            enemy.is_selected  = True 
             
            enemy.update_green_case(self.player_units,self.enemy_units)   
            print(enemy_selected.list_attaques)
>>>>>>> efc26043aee740add8fd16090271b71780076ad3
                # Déplacement aléatoire
            target = random.choice(self.player_units)
            print (target)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

<<<<<<< HEAD

            # Attaque si possible
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)
            enemy.is_selected = False
        self.flip_display() 
        play = True
        return play 
=======
            enemy_attack = random.choice(enemy_selected.list_attaques)
            print(enemy_attack)

            indice = enemy_selected.list_attaques.index(enemy_attack)
            print(indice)
            enemy_attack_selected = enemy_selected.attribuer_class_attaque(indice)

            # Attaque si possible
            for i, player in enumerate(self.player_units) :
                player_selected = player.attribuer_class_perso()  
                player_health = self.list_player_health[i]
                print (f"POUR L'INSTANT : {player_health}")
                                                
                new_player_health = enemy_selected.attack(enemy_attack_selected, player_selected, player_health)
                                                    

                print (f"AILLLEE T'AS PRIS CHER!!!! IL TE RESTE {new_player_health} POINTS DE VIE !!!")
                self.list_player_health[i] = new_player_health

                if player_health <= 0:
                    print(f"{player.name} est mort")
                    self.player_units.remove(player)
                
                self.flip_display()

            enemy.is_selected = False
         
        play = True
        return play, self.list_player_health
>>>>>>> efc26043aee740add8fd16090271b71780076ad3

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
                pygame.draw.rect(self.screen, WHITE, rect, -1)

        # Ajoutez les sprites des unités/players
<<<<<<< HEAD
        for unit in self.player_units + self.enemy_units :
            unit.draw(self.screen)
            if unit.is_selected :
                unit.draw_green_case(self.screen)
                if self.menu_attaques:
                    unit.draw_red_case(self.screen)
                print (f"l'unité est : {unit.name}, {unit.defense}")


        #for unit in self.enemy_units :
        #    unit.draw(self.screen)
        #    unit.draw_green_case(self.screen)
            
=======
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

>>>>>>> efc26043aee740add8fd16090271b71780076ad3

         # Si le menu des attaques est actif, dessiner le menu par-dessus
        if self.menu_attaques:  
            self.draw_attack_menu()

        if all(health <= 0 for health in self.list_enemy_health):
            print("Tous les ennemis ont été éliminés !")
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Victoire !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Victoire !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
            pygame.display.flip()
            pygame.time.wait(3000)  # Pause de 3 secondes avant de quitter
            
        elif all(health <= 0 for health in self.list_player_health):
            print("Tous les ennemis ont été éliminés !")
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 119)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 121)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2 + 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_black('Defaite !', 70, self.DISPLAY_W / 2 - 3, self.DISPLAY_H / 2 - 120)
            self.draw_text_white('Defaite !', 70, self.DISPLAY_W / 2, self.DISPLAY_H / 2 - 120)
        
   
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
    screen = pygame.display.set_mode((WIDTH , HEIGHT))
    pygame.display.set_caption("Marvel Game")
    
    # Instanciation du jeu
    game = Game(screen)

    while game.running:
        game.curr_menu.display_menu()
        if (game.playing):
            break
    
<<<<<<< HEAD
    game.player_units = [Unit(game.Choix_Personnages_1.game_personnage, 0, 0, [55,55]),#,150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_2.game_personnage, 0, 1, [55,55])]#, 150 , 3, 75, ["Poings", "Lancer_bouclier"] )]                  

    game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 16, 9, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit(game.Choix_Personnages_4.game_personnage, 17, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]
    
=======
    
    #game.player_units = [Unit(game.Choix_Personnages_1.game_personnage, 0, 0, [55,55]),#,150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             #Unit(game.Choix_Personnages_2.game_personnage, 0, 1, [55,55])]#, 150 , 3, 75, ["Poings", "Lancer_bouclier"] )]                  
    player1 = Unit(game.Choix_Personnages_1.game_personnage, 0, 0, [55,55], game)
    hero1 = player1.attribuer_class_perso()
    if hero1 :
        hero_health1 = hero1.get_health()
    game.player_units.append(player1)
    game.list_player_health.append(hero_health1)
    player2 = Unit(game.Choix_Personnages_2.game_personnage, 0, 1, [55,55], game)
    hero2 = player2.attribuer_class_perso()
    hero_health2 = hero2.get_health() 
    game.player_units.append(player2)
    game.list_player_health.append(hero_health2) 
        
    print (f"NBRE DE POINTS DE VIE DE {player1.name} = {hero_health1}")
    print (f"NBRE DE POINTS DE VIE DE {player2.name} = {hero_health2}")


    #game.enemy_units = [Unit(game.Choix_Personnages_3.game_personnage, 0, 9, [55,55]),#, 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             #Unit(game.Choix_Personnages_4.game_personnage, 1, 9, [55,55])]#, 150, 3, 75, ["Poings", "Lancer_bouclier"] )]

    player3 = Unit(game.Choix_Personnages_3.game_personnage, 0, 9, [55,55], game)
    hero3 = player3.attribuer_class_perso()
    hero_health3 = hero3.get_health()
    game.enemy_units.append(player3)
    game.list_enemy_health.append(hero_health3)
    player4 = Unit(game.Choix_Personnages_4.game_personnage, 1, 9, [55,55], game)
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

>>>>>>> efc26043aee740add8fd16090271b71780076ad3
    play = True
    iter = 0
    
    # Boucle principale du jeu
    while play and iter<100 :
        game.handle_player_turn()
<<<<<<< HEAD
        game.handle_enemy_turn()   
        iter += 1 
        play =  game.handle_enemy_turn() 
=======
        if game.Mode_jeu :
            game.handle_enemy_turn()  
        else :
            game.handle_player_2_turn()
        iter += 1    
>>>>>>> efc26043aee740add8fd16090271b71780076ad3

if __name__ == "__main__":
    main()
