import pygame


class Player(pygame.sprite.Sprite):
    
    #--------------------- init function -------------------------
    def __init__(self,x,y,size):
        #initial condition
        super().__init__()
        self.x=x
        self.y=y
        self.size=size
        self.image = pygame.Surface(size)
        self.position=[x,y]
        
        
<<<<<<< Updated upstream
        # add the player      
        self.sprite_sheet=pygame.image.load('4_fantastic.png') 
        self.image=self.get_image(0,0) # get image in this coordinate
=======
        # add the player     
        self.sprite_sheet=pygame.image.load('Marvel.png') 
        self.image=self.get_image(self.x,self.y) # get image in this coordinate
>>>>>>> Stashed changes
        self.image=pygame.transform.scale(self.image,(32,32))
        self.image.set_colorkey([0,0,0]) # to remove the withe color of the background
        self.rect=pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object
        
        
        # collision between player and obstacle
        self.feet=pygame.Rect(0,0,self.rect.width*0.3,30) # rectangle focus on the feet of the player
        self.old_position=self.position.copy()
    
        
    #--------------------- functions ----------------------------  
    
    def save_location(self):  # before mooving the player 
        self.old_position = self.position.copy()
     
    def move_x(self,velocity): # move player on x-axis
        self.position[0]+=velocity
        
    def move_y(self,velocity): # move player on y-axis
        self.position[1]+=velocity
        
    def update(self): # update for collision
        self.rect.topleft=self.position  
        self.feet.midbottom= self.rect.midbottom
        
    def move_back(self): # move back when collision
        self.position=self.old_position
        self.rect.topleft=self.position  
        self.feet.midbottom= self.rect.midbottom
        
    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([42,52])
        image.blit(self.sprite_sheet,(0,0),(x,y,42,52))
        return image
    
    
