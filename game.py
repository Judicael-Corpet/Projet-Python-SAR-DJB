import pygame 
import random
import pytmx
import pyscroll
from unit import *
#from menu import *
#from sound import 

personnages = ["Captain_America", "Hulk", "Ironman", "Spiderman", "Thor", "Groot", "Wolverine", "Black_Panther", 
                            "Starlord", "Yondu", "Torch", "Jane_Storm", "Chose", "Dr_Strange"]
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
        self.screen = screen
        self.selected_attack_index = 0  # Indice de l'attaque sélectionnée
        self.attaques = ["Poings", "Griffes", "Lancer_bouclier", "Casser_les_murs", "Laser", "Missile", "Bloquer_adversaire", "Attaque_toile", "Marteau", "Foudre", "Attaque_Branche", "Protection", "Pistolets", "Fleche_Yaka", "Boule_De_Feu", "Soigner", "Projectile" ]
        self.menu_attaques = False
        self.selected_attack = False


        self.player_units = [Unit("Captain_America", 0, 0, [55,55],150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit("Captain_America", 0, 1, [55,55], 150 , 3, 75, ["Poings", "Lancer_bouclier"] )]                   

        self.enemy_units = [Unit("Captain_America", 16, 9, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"] ), 
                             Unit("Captain_America", 17, 9, [55,55], 150, 3, 75, ["Poings", "Lancer_bouclier"] )]

    def selection_personnages(self, liste_perso) :
          
        for i in range(3) :
            self.list_names.append(random.choice(liste_perso))
        return self.list_names    

    def draw_attack_menu(self) :
        """Dessine le menu des attaques."""
        #Fond noir dans le coin inférieur gauche
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 340, 250, 600 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 340, 250, 600), 2)  # Bordure blanche

        #if selected_unit == "Captain_America" :
        self.attaques = ["Poings", "Lancer_bouclier"]
        
        # Dessiner chaque attaque dans le rectangle
        for i, attaque in enumerate(self.attaques):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Mettre en surbrillance l'attaque sélectionnée
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 350 + i * 30))  # Positionnement des attaques
  

    def handle_player_turn(self):
        """Tour du joueur"""

        
        for selected_unit in self.player_units:

            # Tant que l'unité n'a pas terminé son tour
            has_acted = False
            selected_unit.is_selected = True
            selected_unit.update_green_case(self.screen,self.player_units,self.enemy_units)
            
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
                        self.flip_display()
                        

                        # Attaque (touche espace) met fin au tour
                        if event.key == pygame.K_SPACE:
                            
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

#Suite du code à écrire ici pour pour appliquer l'attaque à l'ennemi ciblé
                        
                        #if self.selected_attack :
                                

                                self.selected_attack = False
                                has_acted = True
                                selected_unit.update_green_case(self.screen,self.player_units,self.enemy_units)
                                selected_unit.is_selected = False 

                        self.flip_display()    
                
                

                            #print(f"Attaque choisie : {attack['name']}")
                            #for enemy in self.enemy_units:
                            #    if abs(selected_unit.x - enemy.x) <= 1 and abs(selected_unit.y - enemy.y) <= 1:
                            #        selected_unit.attack(enemy)
                            #        if enemy.health <= 0:
                            #            self.enemy_units.remove(enemy)

                            
                
                        

    def handle_enemy_turn(self):
        """IA très simple pour les ennemis."""
        for enemy in self.enemy_units:

            # Déplacement aléatoire
            target = random.choice(self.player_units)
            dx = 1 if enemy.x < target.x else -1 if enemy.x > target.x else 0
            dy = 1 if enemy.y < target.y else -1 if enemy.y > target.y else 0
            enemy.move(dx, dy)

            # Attaque si possible
            if abs(enemy.x - target.x) <= 1 and abs(enemy.y - target.y) <= 1:
                enemy.attack(target)
                if target.health <= 0:
                    self.player_units.remove(target)

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
                pygame.draw.rect(self.screen, WHITE, rect, -1)

        # Ajoutez les sprites des unités/players
        for unit in self.player_units + self.enemy_units:
            unit.draw(self.screen)
            unit.draw_green_case(self.screen)

         # Si le menu des attaques est actif, dessiner le menu par-dessus
        if self.menu_attaques:  
            self.draw_attack_menu()
   
        pygame.display.flip()

        

def main():

    # Initialisation de Pygame
    pygame.init()
    
    # Instanciation de la fenêtre
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Mon jeu de stratégie")
    
    # Instanciation du jeu
    game = Game(screen)

    # Boucle principale du jeu
    while True:
        
        game.handle_player_turn()
        game.handle_enemy_turn()  
        

if __name__ == "__main__":
    main()
