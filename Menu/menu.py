import pygame
from sound import SoundManager
from game import *

fond = pygame.image.load('Menu/Fond_ecran.png')

captain = pygame.image.load('Menu/Personnages_menu/captain_america_menu.jpeg')
captain2 = pygame.transform.scale(captain, (200, 200))
#captain2.set_colorkey((255, 255, 255))
hulk = pygame.image.load('Menu/Personnages_menu/hulk_menu.jpeg')
hulk2 = pygame.transform.scale(hulk, (200, 200))
#hulk2.set_colorkey((255, 255, 255))
ironman = pygame.image.load('Menu/Personnages_menu/ironman_menu.jpeg')
ironman2 = pygame.transform.scale(ironman, (200, 200))

Spiderman = pygame.image.load('Menu/Personnages_menu/spiderman_menu.png')
Spiderman2 = pygame.transform.scale(Spiderman, (200, 200))

Thor = pygame.image.load('Menu/Personnages_menu/thor_menu.jpeg')
Thor2 = pygame.transform.scale(Thor, (200, 200))

Groot = pygame.image.load('Menu/Personnages_menu/groot_menu.jpeg')
Groot2 = pygame.transform.scale(Groot, (200, 200))

Wolverine = pygame.image.load('Menu/Personnages_menu/wolverine_menu.jpeg')
Wolverine2 = pygame.transform.scale(Wolverine, (200, 200))

Panther = pygame.image.load('Menu/Personnages_menu/black_panther_menu.jpeg')
Panther2 = pygame.transform.scale(Panther, (200, 200))

Starlord = pygame.image.load('Menu/Personnages_menu/starlord_menu.jpeg')
Starlord2 = pygame.transform.scale(Starlord, (200, 200))

Yondu = pygame.image.load('Menu/Personnages_menu/yondu_menu.jpeg')
Yondu2 = pygame.transform.scale(Yondu, (200, 200))

Torch = pygame.image.load('Menu/Personnages_menu/torch_menu.jpeg')
Torch2 = pygame.transform.scale(Torch, (200, 200))

Jane = pygame.image.load('Menu/Personnages_menu/jane_storm_menu.png')
Jane2 = pygame.transform.scale(Jane, (200, 200))

Chose = pygame.image.load('Menu/Personnages_menu/chose_menu.png')
Chose2 = pygame.transform.scale(Chose, (200, 200))

Strange = pygame.image.load('Menu/Personnages_menu/docteur_strange_menu.jpeg')
Strange2 = pygame.transform.scale(Strange, (200, 200))


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
        
    def draw_cursor(self):
        self.game.draw_text_black('*', 50, self.cursor_rect.x - 2, self.cursor_rect.y)
        self.game.draw_text_black('*', 50, self.cursor_rect.x + 2, self.cursor_rect.y)
        self.game.draw_text_black('*', 50, self.cursor_rect.x, self.cursor_rect.y - 2)
        self.game.draw_text_black('*', 50, self.cursor_rect.x, self.cursor_rect.y + 2)
        self.game.draw_text_white('*', 50, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0)) 
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 30)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(fond, (0, 0))

            self.game.draw_text_black('Marvel Games', 140, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 150)
            self.game.draw_text_black('Marvel Games', 140, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 150)
            self.game.draw_text_black('Marvel Games', 140, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 147)
            self.game.draw_text_black('Marvel Games', 140, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 153)
            self.game.draw_text_white('Marvel Games', 140, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 150)

            self.game.draw_text_black('Menu', 100, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 10)
            self.game.draw_text_black('Menu', 100, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 10)
            self.game.draw_text_black('Menu', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 13)
            self.game.draw_text_black('Menu', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 7)
            self.game.draw_text_white('Menu', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 10)
            
            self.game.draw_text_black("Start Game", 30, self.startx + 1, self.starty + 20)
            self.game.draw_text_black("Start Game", 30, self.startx - 1, self.starty + 20)
            self.game.draw_text_black("Start Game", 30, self.startx, self.starty + 21)
            self.game.draw_text_black("Start Game", 30, self.startx, self.starty + 19)
            self.game.draw_text_white("Start Game", 30, self.startx, self.starty + 20)
            
            self.game.draw_text_black("Options", 30, self.optionsx + 1, self.optionsy + 40)
            self.game.draw_text_black("Options", 30, self.optionsx - 1, self.optionsy + 40)
            self.game.draw_text_black("Options", 30, self.optionsx, self.optionsy + 39)
            self.game.draw_text_black("Options", 30, self.optionsx, self.optionsy + 41)
            self.game.draw_text_white("Options", 30, self.optionsx, self.optionsy + 40)

            self.game.draw_text_black("Credits", 30, self.creditsx + 1, self.creditsy + 60)
            self.game.draw_text_black("Credits", 30, self.creditsx - 1, self.creditsy + 60)
            self.game.draw_text_black("Credits", 30, self.creditsx, self.creditsy + 59)
            self.game.draw_text_black("Credits", 30, self.creditsx, self.creditsy + 61)
            self.game.draw_text_white("Credits", 30, self.creditsx, self.creditsy + 60)

            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy + 50)
                self.state = 'Options'
                self.game.sound_manager.bruit('Blop')
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy + 70)
                self.state = 'Credits'
                self.game.sound_manager.bruit('Blop')
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 30)
                self.state = 'Start'
                self.game.sound_manager.bruit('Blop')
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy + 70)
                self.state = 'Credits'
                self.game.sound_manager.bruit('Blop')
            elif self.state == 'Options':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty + 30)
                self.state = 'Start'
                self.game.sound_manager.bruit('Blop')
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy + 50)
                self.state = 'Options'
                self.game.sound_manager.bruit('Blop')

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.Choix_Personnages
                if self.game.Musique :
                    self.game.sound_manager.bruit('Musique_lancement')
                    #pygame.mixer.music.play(-1)  # Lecture en boucle infinie (-1)
                #self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class Choix_Personnage_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Captain_America'
        self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 150, self.game.DISPLAY_H / 3 + 10)

    def display_menu(self):
        self.run_display = True
        prev_state = None
        while self.run_display:
            self.game.check_events()
            self.check_input()
            if self.state != prev_state:
                self.game.display.blit(fond, (0, 0))
            
                self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 249)
                self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 251)
                self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 250)
                self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 250)
                self.game.draw_text_white('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 250)

                self.game.draw_text_black("Captain America", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 - 2)
                self.game.draw_text_black("Captain America", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 2)
                self.game.draw_text_black("Captain America", 30, self.game.DISPLAY_W / 3 + self.offset - 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_black("Captain America", 30, self.game.DISPLAY_W / 3 + self.offset + 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_white("Captain America", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3)

                self.game.draw_text_black("Hulk", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 62)
                self.game.draw_text_black("Hulk", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 58)
                self.game.draw_text_black("Hulk", 30, self.game.DISPLAY_W / 3 + self.offset - 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_black("Hulk", 30, self.game.DISPLAY_W / 3 + self.offset + 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_white("Hulk", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 60)

                self.game.draw_text_black("Ironman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 118)
                self.game.draw_text_black("Ironman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 122)
                self.game.draw_text_black("Ironman", 30, self.game.DISPLAY_W / 3 + self.offset - 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_black("Ironman", 30, self.game.DISPLAY_W / 3 + self.offset + 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_white("Ironman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 120)

                self.game.draw_text_black("Spiderman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 180 - 2)
                self.game.draw_text_black("Spiderman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 180 + 2)
                self.game.draw_text_black("Spiderman", 30, self.game.DISPLAY_W / 3 + self.offset - 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_black("Spiderman", 30, self.game.DISPLAY_W / 3 + self.offset + 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_white("Spiderman", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 180)

                self.game.draw_text_black("Thor", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 - 2 + 240)
                self.game.draw_text_black("Thor", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 2 + 240)
                self.game.draw_text_black("Thor", 30, self.game.DISPLAY_W / 3 + self.offset - 2, self.game.DISPLAY_H / 3 + 240)
                self.game.draw_text_black("Thor", 30, self.game.DISPLAY_W / 3 + self.offset + 2, self.game.DISPLAY_H / 3 + 240)
                self.game.draw_text_white("Thor", 30, self.game.DISPLAY_W / 3 + self.offset, self.game.DISPLAY_H / 3 + 240)

                self.game.draw_text_black("Groot", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 2)
                self.game.draw_text_black("Groot", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 2)
                self.game.draw_text_black("Groot", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_black("Groot", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_white("Groot", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3)

                self.game.draw_text_black("Wolverine", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 62)
                self.game.draw_text_black("Wolverine", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 58)
                self.game.draw_text_black("Wolverine", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_black("Wolverine", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_white("Wolverine", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 60)

                self.game.draw_text_black("Black Panther", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 120 - 2)
                self.game.draw_text_black("Black Panther", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 120 + 2)
                self.game.draw_text_black("Black Panther", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_black("Black Panther", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_white("Black Panther", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 120)

                self.game.draw_text_black("Starlord", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 2 + 180)
                self.game.draw_text_black("Starlord", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 2 + 180)
                self.game.draw_text_black("Starlord", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_black("Starlord", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_white("Starlord", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 180)

                self.game.draw_text_black("Yondu", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 2 + 240)
                self.game.draw_text_black("Yondu", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 2 + 240)
                self.game.draw_text_black("Yondu", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3 + 240)
                self.game.draw_text_black("Yondu", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3 + 240)
                self.game.draw_text_white("Yondu", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 240)

                self.game.draw_text_black("Torch", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 - 2)
                self.game.draw_text_black("Torch", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 2)
                self.game.draw_text_black("Torch", 30, 2*self.game.DISPLAY_W / 3 - self.offset - 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_black("Torch", 30, 2*self.game.DISPLAY_W / 3 - self.offset + 2, self.game.DISPLAY_H / 3)
                self.game.draw_text_white("Torch", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3)

                self.game.draw_text_black("Jane Storm", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 - 2 + 60)
                self.game.draw_text_black("Jane Storm", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 2 + 60)
                self.game.draw_text_black("Jane Storm", 30, 2*self.game.DISPLAY_W / 3 - self.offset - 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_black("Jane Storm", 30, 2*self.game.DISPLAY_W / 3 - self.offset + 2, self.game.DISPLAY_H / 3 + 60)
                self.game.draw_text_white("Jane Storm", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 60)

                self.game.draw_text_black("Chose", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 - 2 + 120)
                self.game.draw_text_black("Chose", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 2 + 120)
                self.game.draw_text_black("Chose", 30, 2*self.game.DISPLAY_W / 3 - self.offset - 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_black("Chose", 30, 2*self.game.DISPLAY_W / 3 - self.offset + 2, self.game.DISPLAY_H / 3 + 120)
                self.game.draw_text_white("Chose", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 120)

                self.game.draw_text_black("Dr_Strange", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 - 2 + 180)
                self.game.draw_text_black("Dr_Strange", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 2 + 180)
                self.game.draw_text_black("Dr_Strange", 30, 2*self.game.DISPLAY_W / 3 - self.offset - 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_black("Dr_Strange", 30, 2*self.game.DISPLAY_W / 3 - self.offset + 2, self.game.DISPLAY_H / 3 + 180)
                self.game.draw_text_white("Dr_Strange", 30, 2*self.game.DISPLAY_W / 3 - self.offset, self.game.DISPLAY_H / 3 + 180)

                self.game.draw_text_black("Back", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 2 + 300)
                self.game.draw_text_black("Back", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 - 2 + 300)
                self.game.draw_text_black("Back", 30, self.game.DISPLAY_W / 2 - 2, self.game.DISPLAY_H / 3 + 300)
                self.game.draw_text_black("Back", 30, self.game.DISPLAY_W / 2 + 2, self.game.DISPLAY_H / 3 + 300)
                self.game.draw_text_white("Back", 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 3 + 300)

                self.draw_cursor()
                self.blit_screen()
            
            if self.state == 'Captain_America':
                self.game.window.blit(captain2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Hulk':
                self.game.window.blit(hulk2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Ironman':
                self.game.window.blit(ironman2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Spiderman':
                self.game.window.blit(Spiderman2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Thor':
                self.game.window.blit(Thor2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Groot':
                self.game.window.blit(Groot2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Wolverine':
                self.game.window.blit(Wolverine2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Black_Panther':
                self.game.window.blit(Panther2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Starlord':
                self.game.window.blit(Starlord2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Yondu':
                self.game.window.blit(Yondu2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Torch':
                self.game.window.blit(Torch2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Jane_Storm':
                self.game.window.blit(Jane2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Chose':
                self.game.window.blit(Chose2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Dr_Strange':
                self.game.window.blit(Strange2, (2*self.game.DISPLAY_W / 3, 450))
            
            pygame.display.flip()
            prev_state = self.state


    def move_cursor(self):

        if self.game.DOWN_KEY:
            if self.state == 'Captain_America':
                self.state = 'Hulk'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 60 + 10)
            elif self.state == 'Hulk':
                self.state = 'Ironman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Ironman':
                self.state = 'Spiderman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Spiderman':
                self.state = 'Thor'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 240 + 10)
            elif self.state == 'Thor':
                self.state = 'Groot'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 10)
            elif self.state == 'Groot':
                self.state = 'Wolverine'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 60 + 10)
            elif self.state == 'Wolverine':
                self.state = 'Black_Panther'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Black_Panther':
                self.state = 'Starlord'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Starlord':
                self.state = 'Yondu'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 240 + 10)
            elif self.state == 'Yondu':
                self.state = 'Torch'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 10)
            elif self.state == 'Torch':
                self.state = 'Jane_Storm'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 60+ 10)
            elif self.state == 'Jane_Storm':
                self.state = 'Chose'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Chose':
                self.state = 'Dr_Strange'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Dr_Strange':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 300 + 10)
            elif self.state == 'Back':
                self.state = 'Captain_America'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 10)

        elif self.game.UP_KEY :
            if self.state == 'Hulk':
                self.state = 'Captain_America'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 10)
            elif self.state == 'Ironman':
                self.state = 'Hulk'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 60 + 10)
            elif self.state == 'Spiderman':
                self.state = 'Ironman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Thor':
                self.state = 'Spiderman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Groot':
                self.state = 'Thor'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.game.DISPLAY_W / 3 + self.offset - 140, self.game.DISPLAY_H / 3 + 240 + 10)
            elif self.state == 'Wolverine':
                self.state = 'Groot'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 10)
            elif self.state == 'Black_Panther':
                self.state = 'Wolverine'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 60 + 10)
            elif self.state == 'Starlord':
                self.state = 'Black_Panther'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Yondu':
                self.state = 'Starlord'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Torch':
                self.state = 'Yondu'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 240 + 10)
            elif self.state == 'Jane_Storm':
                self.state = 'Torch'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 10)
            elif self.state == 'Chose':
                self.state = 'Jane_Storm'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 60 + 10)
            elif self.state == 'Dr_Strange':
                self.state = 'Chose'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 120 + 10)
            elif self.state == 'Back':
                self.state = 'Dr_Strange'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (2*self.game.DISPLAY_W / 3 + self.offset + 100, self.game.DISPLAY_H / 3 + 180 + 10)
            elif self.state == 'Captain_America':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.mid_w + self.offset - 10, self.game.DISPLAY_H / 3 + 300 + 10)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            """
            if self.state == 'Yes':
                self.game.curr_menu = self.game.Choix_Carte
            """
            if self.state == 'Captain_America':
                self.game.window.blit(captain2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Hulk':
                self.game.window.blit(hulk2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Ironman':
                self.game.window.blit(ironman2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Spiderman':
                self.game.window.blit(Spiderman2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Thor':
                self.game.window.blit(Thor2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Groot':
                self.game.window.blit(Groot2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Wolverine':
                self.game.window.blit(Wolverine2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Black_Panther':
                self.game.window.blit(Panther2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Starlord':
                self.game.window.blit(Starlord2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Yondu':
                self.game.window.blit(Yondu2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Torch':
                self.game.window.blit(Torch2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Jane_Storm':
                self.game.window.blit(Jane2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Chose':
                self.game.window.blit(Chose2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Dr_Strange':
                self.game.window.blit(Strange2, (2*self.game.DISPLAY_W / 3, 450))
            elif self.state == 'Back':
                self.game.curr_menu = self.game.main_menu
                self.game.START_KEY = False
                pygame.mixer.music.stop()
                self.run_display = False

class Choix_Carte_Menu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Yes'
        self.volx, self.voly = self.mid_w, self.mid_h
        self.backx, self.backy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly  + 10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY and (self.cursor_rect.midtop == (self.volx + self.offset, self.voly)):
                self.game.curr_menu = self.game.main_menu
            self.check_input()
            self.game.display.blit(fond, (0, 0))
            
            self.game.draw_text_black('Choix carte', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 229)
            self.game.draw_text_black('Choix carte', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 231)
            self.game.draw_text_black('Choix carte', 100, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_black('Choix carte', 100, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_white('Choix carte', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 230)

            self.game.draw_text_black("Yes", 50, self.volx, self.voly - 2)
            self.game.draw_text_black("Yes", 50, self.volx, self.voly + 2)
            self.game.draw_text_black("Yes", 50, self.volx - 2, self.voly)
            self.game.draw_text_black("Yes", 50, self.volx + 2, self.voly)
            self.game.draw_text_white("Yes", 50, self.volx, self.voly)

            self.game.draw_text_black("No", 50, self.backx, self.backy - 2)
            self.game.draw_text_black("No", 50, self.backx, self.backy + 2)
            self.game.draw_text_black("No", 50, self.backx - 2, self.backy)
            self.game.draw_text_black("No", 50, self.backx + 2, self.backy)
            self.game.draw_text_white("No", 50, self.backx, self.backy)

            self.game.draw_text_black("Back", 50, self.backx, self.backy + 58)
            self.game.draw_text_black("Back", 50, self.backx, self.backy + 62)
            self.game.draw_text_black("Back", 50, self.backx - 2, self.backy + 60)
            self.game.draw_text_black("Back", 50, self.backx + 2, self.backy + 60)
            self.game.draw_text_white("Back", 50, self.backx, self.backy + 60)

            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Yes':
                self.state = 'No'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)
            elif self.state == 'No':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Back':
                self.state = 'Yes'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            
        elif self.game.UP_KEY :
            if self.state == 'Yes':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'No':
                self.state = 'Yes'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Back':
                self.state = 'No'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'No':
                self.game.Musique = False
            elif self.state == 'Back':
                self.game.curr_menu = self.game.options
            self.run_display = False

class Volume(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Yes'
        self.volx, self.voly = self.mid_w, self.mid_h
        self.backx, self.backy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly  + 10)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY and (self.cursor_rect.midtop == (self.volx + self.offset, self.voly)):
                self.game.curr_menu = self.game.main_menu
            self.check_input()
            self.game.display.blit(fond, (0, 0))
            
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 229)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 231)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_white('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 230)

            self.game.draw_text_black("Yes", 50, self.volx, self.voly - 2)
            self.game.draw_text_black("Yes", 50, self.volx, self.voly + 2)
            self.game.draw_text_black("Yes", 50, self.volx - 2, self.voly)
            self.game.draw_text_black("Yes", 50, self.volx + 2, self.voly)
            self.game.draw_text_white("Yes", 50, self.volx, self.voly)

            self.game.draw_text_black("No", 50, self.backx, self.backy - 2)
            self.game.draw_text_black("No", 50, self.backx, self.backy + 2)
            self.game.draw_text_black("No", 50, self.backx - 2, self.backy)
            self.game.draw_text_black("No", 50, self.backx + 2, self.backy)
            self.game.draw_text_white("No", 50, self.backx, self.backy)

            self.game.draw_text_black("Back", 50, self.backx, self.backy + 58)
            self.game.draw_text_black("Back", 50, self.backx, self.backy + 62)
            self.game.draw_text_black("Back", 50, self.backx - 2, self.backy + 60)
            self.game.draw_text_black("Back", 50, self.backx + 2, self.backy + 60)
            self.game.draw_text_white("Back", 50, self.backx, self.backy + 60)

            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Yes':
                self.state = 'No'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)
            elif self.state == 'No':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Back':
                self.state = 'Yes'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            
        elif self.game.UP_KEY :
            if self.state == 'Yes':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'No':
                self.state = 'Yes'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Back':
                self.state = 'No'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Yes':
                self.game.Musique = True         
            elif self.state == 'No':
                self.game.Musique = False
            elif self.state == 'Back':
                self.game.curr_menu = self.game.options
            self.run_display = False
class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Volume"
        self.volx, self.voly = self.mid_w, self.mid_h
        self.backx, self.backy = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly  + 10)
        
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(fond, (0, 0))
            
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 229)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 231)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_black('Options', 150, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_white('Options', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 230)

            self.game.draw_text_black("Volume", 50, self.volx, self.voly - 2)
            self.game.draw_text_black("Volume", 50, self.volx, self.voly + 2)
            self.game.draw_text_black("Volume", 50, self.volx - 2, self.voly)
            self.game.draw_text_black("Volume", 50, self.volx + 2, self.voly)
            self.game.draw_text_white("Volume", 50, self.volx, self.voly)

            self.game.draw_text_black("Back", 50, self.backx, self.backy - 2)
            self.game.draw_text_black("Back", 50, self.backx, self.backy + 2)
            self.game.draw_text_black("Back", 50, self.backx - 2, self.backy)
            self.game.draw_text_black("Back", 50, self.backx + 2, self.backy)
            self.game.draw_text_white("Back", 50, self.backx, self.backy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Volume':
                self.state = 'Back'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)
            elif self.state == 'Back':
                self.state = 'Volume'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.volx + self.offset, self.voly + 10)
        elif self.game.START_KEY and self.state == 'Volume':
            self.game.curr_menu = self.game.Volume
            self.run_display = False
        elif self.game.START_KEY and self.state == 'Back':
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.blit(fond, (0, 0))

            self.game.draw_text_black('Credits', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 229)
            self.game.draw_text_black('Credits', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 231)
            self.game.draw_text_black('Credits', 150, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_black('Credits', 150, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_white('Credits', 150, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 230)

            self.game.draw_text_black('Made by Baptiste', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 119)
            self.game.draw_text_black('Made by Baptiste', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 121)
            self.game.draw_text_black('Made by Baptiste', 70, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text_black('Made by Baptiste', 70, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 120)
            self.game.draw_text_white('Made by Baptiste', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 120)

            self.game.draw_text_black('Made by Dan', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 39)
            self.game.draw_text_black('Made by Dan', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 41)
            self.game.draw_text_black('Made by Dan', 70, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text_black('Made by Dan', 70, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 40)
            self.game.draw_text_white('Made by Dan', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 40)

            self.game.draw_text_black('Made by Judicael', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 39)
            self.game.draw_text_black('Made by Judicael', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 41)
            self.game.draw_text_black('Made by Judicael', 70, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text_black('Made by Judicael', 70, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text_white('Made by Judicael', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)

            self.game.draw_text_black('Back - Press Enter -', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 119)
            self.game.draw_text_black('Back - Press Enter -', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 121)
            self.game.draw_text_black('Back - Press Enter -', 70, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 + 120)
            self.game.draw_text_black('Back - Press Enter -', 70, self.game.DISPLAY_W / 2 - 3 , self.game.DISPLAY_H / 2 + 120)
            self.game.draw_text_white('Back - Press Enter -', 70, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)

            self.draw_cursor()
            self.blit_screen()




