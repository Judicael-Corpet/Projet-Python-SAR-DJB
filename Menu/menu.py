import pygame
from sound import SoundManager
from game import *

fond = pygame.image.load('Menu\Fond_ecran.png')

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
        self.game.window.blit(self.game.display, (0, 0)) #fond self.game.display
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
                #self.game.playing = True
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False

class Choix_Personnage_Menu(Menu):
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
            
            self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 229)
            self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 231)
            self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2 + 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_black('Choix personnage', 100, self.game.DISPLAY_W / 2 - 3, self.game.DISPLAY_H / 2 - 230)
            self.game.draw_text_white('Choix personnage', 100, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 230)

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
            if self.state == 'Captain_America':
                self.state = 'Hulk'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)
            elif self.state == 'Hulk':
                self.state = 'Ironman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Ironman':
                self.state = 'Spiderman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Spiderman':
                self.state = 'Thor'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Thor':
                self.state = 'Hawkeye'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Hawkeye':
                self.state = 'Wolverine'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Wolverine':
                self.state = 'Black_Panther'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Black_Panther':
                self.state = 'Starlord'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Starlord':
                self.state = 'Deadpool'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Deadpool':
                self.state = 'Torch'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Torch':
                self.state = 'Jane_Storm'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Jane_Storm':
                self.state = 'Chose'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Chose':
                self.state = 'Dr_Strange'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Dr_Strange':
                self.state = 'Captain_America'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)

        elif self.game.UP_KEY :
            if self.state == 'Captain_America':
                self.state = 'Hulk'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 10)
            elif self.state == 'Hulk':
                self.state = 'Ironman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Ironman':
                self.state = 'Spiderman'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Spiderman':
                self.state = 'Thor'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Thor':
                self.state = 'Hawkeye'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Hawkeye':
                self.state = 'Wolverine'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Wolverine':
                self.state = 'Black_Panther'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Black_Panther':
                self.state = 'Starlord'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Deadpool':
                self.state = 'Starlord'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.backy + 70)
            elif self.state == 'Torch':
                self.state = 'Deadpool'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Jane_Storm':
                self.state = 'Torch'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Chose':
                self.state = 'Jane_Storm'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Dr_Strange':
                self.state = 'Chose'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)
            elif self.state == 'Captain_America':
                self.state = 'Dr_Strange'
                self.game.sound_manager.bruit('Blop')
                self.cursor_rect.midtop = (self.backx + self.offset, self.voly + 10)

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Yes':
                self.game.curr_menu = self.game.Choix_Carte
            elif self.state == 'No':
                self.game.Musique = False
            elif self.state == 'Back':
                self.game.curr_menu = self.game.options
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
            if self.game.START_KEY and (self.cursor_rect.midtop == (self.backx + self.offset, self.backy)):
                self.game.curr_menu = self.game.main_menu
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




