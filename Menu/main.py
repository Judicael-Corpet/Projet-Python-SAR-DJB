from game import Game
from menu import *

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop() #test 2
