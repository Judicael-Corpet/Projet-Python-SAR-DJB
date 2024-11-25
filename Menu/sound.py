import pygame


class SoundManager :
    def __init__(self):
        pygame.init()
        self.sounds = {
            'Blop': pygame.mixer.Sound("Blop.mp3"),
            'Boule_feu' : pygame.mixer.Sound("Boule_feu.dat.mp3")

        }

    def bruit(self, name):
        #self.sounds[name].play()
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Son {name} introuvable.")


"""
sound_manager = SoundManager()
sound_manager.bruit('Blop')
"""