
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
        
        # define list to stock boundary element  
        self.walls = []  # initialize empty list
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        # Player 1 equipe 1
        self.player_x, self.player_y = 0, 0  # spawn player 1 
        self.size = [42, 52]  # size player
        self.player = Player(self.player_x, self.player_y, self.size)
        self.group.add(self.player)

        self.player_velocity_x = 0  # the initial velocity
        self.player_velocity_y = 0

        self.rect = self.window.get_rect()  # Create the window boundary rectangle

        self.clock = pygame.time.Clock()
        self.fps = 30

        
       
        #timer
        self.start_timer=90000 # ms
        self.reset_time=0
    
    
    def update(self):
        self.group.update()
        # verification
        for sprite in self.group.sprites():
            if sprite.feet.collidelist(self.walls) > -1:
                sprite.move_back()
      
    
    
    

    def main_loop(self):

        while self.game_open:
            # map
            self.group.draw(self.window)
             
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # to quit the game
             
                        
                   
                # PLAYER 1
                if event.type == pygame.KEYDOWN:  # key activated
                    if event.key == pygame.K_RIGHT:  # move right
                        self.player_velocity_x = 5  
                        self.player.direction_x = 1
                        
                        
                    if event.key == pygame.K_LEFT:  # move left
                        self.player_velocity_x = -5
                        self.player.direction_x = -1
                        
                        
                    if event.key == pygame.K_UP:  # move up
                        self.player_velocity_y = -5
                        self.player.direction_y = -1
                   
                        
                    if event.key == pygame.K_DOWN:  # move down
                        self.player_velocity_y = 5
                        self.player.direction_y = 1
                        

                        
        
                elif event.type == pygame.KEYUP:  # key deactivated
                    # PLAYER 1
                    if event.key == pygame.K_RIGHT:  # stop the velocity right
                        self.player_velocity_x = 0
                    if event.key == pygame.K_LEFT:  # stop the velocity left
                        self.player_velocity_x = 0
                    if event.key == pygame.K_UP:  # stop move up
                        self.player_velocity_y = 0
                    if event.key == pygame.K_DOWN:  # stop move down
                        self.player_velocity_y = 0
                    
                 
              
                
            self.player.rect.clamp_ip(self.rect) # restreint les coordonnées du joeuur dans le rectangle  de la fenetre window
          
            self.player.save_location()
            self.player.move_x(self.player_velocity_x)
            self.player.move_y(self.player_velocity_y)
            
            
            self.player.update()
            
            for wall in self.walls:
                if self.player.rect.colliderect(wall):  # Collision détectée
                    self.player.move_back()  # Revenir à l'ancienne position
            
            
            
       
            
            #clock
            self.clock.tick(self.fps)  # update clock <= 30 fps
            pygame.display.flip()  # update window each iteration
            
            
 
    
if __name__ == '__main__':
    pygame.init()
    Game().main_loop()
    pygame.quit()









