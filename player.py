import pygame


'''
Position des personnage sur la feuille Marvel
Captain america : (5, 0)
Hulk : (55, 0)
Iron man : (95, 0)
Spiderman : (130, 0)
Thor : (175, 0)

'''


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
        
        
        # add the player 1 team 1    
        self.sprite_sheet=pygame.image.load('Marvel.png') 
        self.image=self.get_image(95,0) # get image in this coordinate
        self.image=pygame.transform.scale(self.image,(32,32))
        self.image.set_colorkey([255,255,255]) # to remove the withe color of the background
        self.rect=pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object
        
        # add the player 2 team 1
        '''
        self.sprite_sheet2=pygame.image.load('Marvel.png') 
        self.image2=self.get_image(55,0) # get image in this coordinate
        self.image2=pygame.transform.scale(self.image,(32,32))
        self.image2.set_colorkey([0,0,0]) # to remove the withe color of the background
        self.rect2=pygame.Rect(self.x,self.y,self.size[0],self.size[1]) # create a rectangle for the player, pygame.Rect() --> create a rectangle object
        
        # case verte possible
        self.green=[]     
        '''   
    
        
    #--------------------- functions ----------------------------  
    
    
     
    def move_x(self, n_case):  # move player on x-axis
        
        new_x=self.position[0]+n_case*32
        if new_x >=0 and new_x<40*32: # pour ne pas aller en dehors de la map
            self.position[0] = new_x
            self.rect.x = self.position[0]  # Update the rectangle's x-coordinate

    def move_y(self, n_case):  # move player on y-axis
        new_y=self.position[1]+ n_case*32
        if new_y>=0 and new_y<25*32:
            self.position[1] = new_y
            self.rect.y = self.position[1]  # Update the rectangle's y-coordinate
        
    def green_case(self,window,position_x,position_y):
        self.green=[] # reinitialisation a chaque appel du tableau
        offsets=[(-32,0),(32,0),(0,-32),(0,32),(32,32),(-32,-32),(-32,32),(32,-32)] # gauche, droite, bas, haut, type :List de TUPLE
        for dx,dy in offsets:
            green_x=position_x +dx
            green_y=position_y+dy
            
            # verifier si green est dans la map et pas en dehors comme pour move_x et move_y
            if green_x >=0 and green_x<40*32 and green_y>=0 and green_y<25*32:
                self.green.append((green_x,green_y))
        
        for i in self.green:
            pygame.draw.rect(window,(0,155,0),(i[0],i[1],32,32)) # case verte
            
            pygame.draw.rect(window, (0, 200, 0), (i[0], i[1], 32, 32), 2)  # bords

        


        
    def get_image(self,x,y): # get image  permet de decouper l'image png du morceau qu'on souhaite
        image=pygame.Surface([42,52])
        image.blit(self.sprite_sheet,(0,0),(x,y,42,52))
        return image
    
    
