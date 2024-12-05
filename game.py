import pygame 
import random
import pytmx
import pyscroll
from unit import *
from menu import *
from attaque import *
from sound import *

fond = pygame.image.load('Fond_ecran.png')

#personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Groot", "Wolverine", "Black_Panther", 
                            #"Starlord", "Yondu", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]



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
        # MENU
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


        # LISTE INSTANCES DE H2ROS

        self.all_heroes = [captain_america, hulk, ironman, spiderman, thor, groot, wolverine, 
              black_panther, starlord, yondu, torch, jane_storm, chose, dr_strange]
        
        # LISTE INSTANCE DE ATTAQUE
        self.all_attaques = [
            aucune_action, poings, griffes, lancer_bouclier, casser_les_murs, laser, missile, 
            bloquer_adversaire, attaque_toile, marteau, foudre, attaque_branche, protection, 
            pistolets, fleche_yaka, boule_de_feu, soigner, projectile]

        
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        self.selected_attack = False

        self.player_units = []
        self.enemy_units = []

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
    
    
    
    def handle_player_turn(self):
        """Tour du joueur""" 
        
        for selected_unit in self.player_units:
            
            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            selected_unit.is_selected = True
            selected_unit.update_green_case(self.player_units,self.enemy_units)
            self.selected_attack_index = 0
            
            
            print (f"l'unité est : {selected_unit.name}, {selected_unit.hero.defense}")
            print(f"Points de vie :{selected_unit.hero.health}, nbre_move = {selected_unit.hero.nbre_move}, defense = {selected_unit.hero.defense}")
        
            
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
                                self.attaques = Attaque()
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
                                    Attaque.attack(self.attaques[self.selected_attack_index], enemy)
                                    
                                    print (enemy.health)
                                        
                                    if enemy.health <= 0 :
                                        print(f"{enemy.hero.name} est mort") 
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

    def handle_enemy_turn(self):
        """IA très simple pour les ennemis."""
       
        
        for enemy in self.enemy_units:
            print (enemy.hero.health)
            enemy.is_selected  = True 
             
            enemy.update_green_case(self.player_units,self.enemy_units)   

                # Déplacement aléatoire
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
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
            perso.draw_perso(self.screen)
            perso.draw_health_bar(self.screen)
            
        for perso1 in self.player_units:
            perso1.draw_perso(self.screen)
            perso1.draw_health_bar(self.screen)
            if perso1.is_selected :
                perso1.draw_green_case(self.screen)
                if self.menu_attaques:
                    perso1.draw_red_case(self.screen)


         # Si le menu des attaques est actif, dessiner le menu par-dessus
        if self.menu_attaques:  
            Attaque.draw_attack_menu(self)
   
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
        
    game.player_units=[]  
    game.enemy_units=[]   
    name1=game.Choix_Personnages_1.game_personnage
    name2=game.Choix_Personnages_2.game_personnage
    name3=game.Choix_Personnages_3.game_personnage
    name4=game.Choix_Personnages_4.game_personnage
    
    for hero in all_heroes:
        if name1==hero.name:
            game.player_units.append(Unit(name1, 0, 0, [55,55],hero))
    
    for hero in all_heroes:
        if name2==hero.name:
            game.player_units.append(Unit(name2, 0, 0, [55,55],hero))        
            
    for hero in all_heroes:
        if name3==hero.name:
            game.enemy_units.append(Unit(name3, 0, 0, [55,55],hero))     
            
    for hero in all_heroes:
        if name3==hero.name:
            game.enemy_units.append(Unit(name4, 0, 0, [55,55],hero))     


    play = True
    iter = 0
    
    # Boucle principale du jeu
    while play and iter<100 :
        game.handle_player_turn()
        game.handle_enemy_turn()   
        
        iter += 1 
         

if __name__ == "__main__":
    main()