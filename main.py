
# all importation
import pygame
import sys, time
import pytmx
import pyscroll
from pygame.sprite import Group
from player import Player




class Game: 
    
    
    
    
    def __init__(self):
        self.window = pygame.display.set_mode((32*40, 32*25))  # height and width screen
        pygame.display.set_caption('')  # set caption
        self.game_open = True
        
        # upload the map
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')  # load the tiled map
        map_data = pyscroll.data.TiledMapData(tmx_data)  # data of the map
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.window.get_size())  # all layer
        # draw layer
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=2)
        self.group2 = pygame.sprite.Group()  # map pas inlcu pour pouvoir gerer player et map 
        
        # Player 1 equipe 1
        self.player_x, self.player_y = 0, 0  # spawn player 1 
        self.size = [42, 52]  # size player
        self.player = Player(self.player_x, self.player_y, self.size) # IMPORTANT 
        self.group2.add(self.player)

        self.player_position_x = 0  # the initial position
        self.player_position_y = 0

        self.rect = self.window.get_rect()  # Create the window boundary rectangle

        self.clock = pygame.time.Clock()
        self.fps = 30

        
       
        #timer
        self.start_timer=90000 # ms
        self.reset_time=0
    
        self.fin_tour=False
        self.entrain_de_jouer=False
        self.old_position=(self.player_position_x,self.player_position_y)

    def main_loop(self):


        while self.game_open:
            # Affichage de la carte 
            self.group.draw(self.window)

            # affichage des cases avant celle du joueur pour qu'on voit le joueur
            self.player.green_case(self.window,self.old_position[0],self.old_position[1])
            
            # Affichage de la carte et joueur --> on affiche deux fois la carte , a ameliorer
            self.group2.draw(self.window)

            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # Quitter le jeu
                
                
                
                
                
                # Déplacements du joueur
                if event.type == pygame.KEYDOWN:  # Appui sur une touche
                    if event.key == pygame.K_RIGHT:  # Droite
                        self.player.move_x(1)  # Déplacement de 32 pixels
                        self.entrain_de_jouer=True
                    elif event.key == pygame.K_LEFT:  # Gauche
                        self.player.move_x(-1)  # Déplacement de -32 pixels
                        self.entrain_de_jouer=True
                    elif event.key == pygame.K_UP:  # Haut
                        self.player.move_y(-1)  # Déplacement vers le haut
                        self.entrain_de_jouer=True
                    elif event.key == pygame.K_DOWN:  # Bas
                        self.player.move_y(1)  # Déplacement vers le bas
                        self.entrain_de_jouer=True
                
                
                
                # deplacement joueur finis
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        print('test: ENTER pressed') # ok ca marche
                        self.fin_tour=True
                        self.old_position=(self.player.rect.x,self.player.rect.y)
                        
            
                                        
            
                
          
            
  
            
            
            
            
            
            
            

            # Mise à jour de l'écran
            self.clock.tick(self.fps)  # Limiter les FPS
            pygame.display.flip()  # Rafraîchir la fenêtre
                    
            
 
    
if __name__ == '__main__':
    pygame.init()
    Game().main_loop()
    pygame.quit()









