
from game import Game
from menu import *
import sys

g = Game()

while g.running:
    g.curr_menu.display_menu()
    #g.game_loop() 
