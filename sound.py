import pygame


class SoundManager :
    def __init__(self):
        pygame.init()
        self.sounds = {
            'Blop': pygame.mixer.Sound("Sons\Blop.mp3"),
            'Boomerang' : pygame.mixer.Sound("Sons\Boomerang.mp3"),
            'Boule_feu' : pygame.mixer.Sound("Sons\Boule_feu.dat.mp3"),
            'Combat' : pygame.mixer.Sound("Sons\Combat.mp3"),
            'Combat_v2' : pygame.mixer.Sound("Sons\Combat_v2.mp3"),
            'Combat_v3' : pygame.mixer.Sound("Sons\Combat_v3.mp3"),
            'Combat_v4' : pygame.mixer.Sound("Sons\Combat_v4.mp3"),
            'Coup_marteau' : pygame.mixer.Sound("Sons\Coup_marteau.mp3"),
            'Coup_poing' : pygame.mixer.Sound("Sons\Coup_poing.mp3"),
            'Feu' : pygame.mixer.Sound("Sons\Feu.mp3"),
            'Fin_jeu' : pygame.mixer.Sound("Sons\Fin_jeu.mp3"),
            'Fleche' : pygame.mixer.Sound("Sons\Fleche.mp3"),
            'Foudre' : pygame.mixer.Sound("Sons\Foudre.mp3"),
            'Foudre_v2' : pygame.mixer.Sound("Sons\Foudre_v2.mp3"),
            'Griffes' : pygame.mixer.Sound("Sons\Griffes.mp3"),
            'Laser' : pygame.mixer.Sound("Sons\Laser.mp3"),
            'Pistolet_silencieux' : pygame.mixer.Sound("Sons\Pistolet_silencieux.mp3"),
            'Revolver' : pygame.mixer.Sound("Sons\Revolver.mp3"),
            'Sabre' : pygame.mixer.Sound("Sons\Sabre.mp3"),
            'Soin' : pygame.mixer.Sound("Sons\Soin.mp3"),
            'Tir_1_coup' : pygame.mixer.Sound("Sons\Tir_1_coup.mp3"),
            'Tir_rafale' : pygame.mixer.Sound("Sons\Tir_rafale.mp3"),
            'Tir_rafale_v2': pygame.mixer.Sound("Sons\Tir_rafale_v2.mp3"),
            'Musique_lancement' : pygame.mixer.Sound("Sons\The_Avengers.mp3")
        }

    def bruit(self, name):
        #self.sounds[name].play()
        if name in self.sounds:
            self.sounds[name].play()
            if self.sounds[name] == 'Musique_lancement':
                pygame.mixer.music.play(-1)
            else :
                self.sounds[name].play()
        else:
            print(f"Son {name} introuvable.")
