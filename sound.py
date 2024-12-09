"""
Ce module gère les sons du jeu en utilisant la bibliothèque pygame.
Il contient la classe SoundManager qui permet de charger et de jouer des sons.
"""

import pygame


class SoundManager :
    def __init__(self):
        pygame.init()
        self.sounds = {
            'A_vos_ordre': pygame.mixer.Sound("Sons/A_vos_ordres.mp3"),
            'Attendre': pygame.mixer.Sound("Sons/Attendre.mp3"),
            'Au_Combat': pygame.mixer.Sound("Sons/Au_Combat.mp3"),
            'Blop': pygame.mixer.Sound("Sons/Blop.mp3"),
            'Boomerang' : pygame.mixer.Sound("Sons/Boomerang.mp3"),
            'Boule_feu' : pygame.mixer.Sound("Sons/Boule_feu.dat.mp3"),
            'Casser_mur' : pygame.mixer.Sound("Sons/Casser_mur.mp3"),
            'Combat' : pygame.mixer.Sound("Sons/Combat.mp3"),
            'Combat_v2' : pygame.mixer.Sound("Sons/Combat_v2.mp3"),
            'Combat_v3' : pygame.mixer.Sound("Sons/Combat_v3.mp3"),
            'Combat_v4' : pygame.mixer.Sound("Sons/Combat_v4.mp3"),
            'Coup_marteau' : pygame.mixer.Sound("Sons/Coup_marteau.mp3"),
            'Coup_poing' : pygame.mixer.Sound("Sons/Coup_poing.mp3"),
            'Ecrasons_ennemi': pygame.mixer.Sound("Sons/Ecrasons_ennemi.mp3"),
            'En_avant': pygame.mixer.Sound("Sons/En_Avant.mp3"),
            'Explosion': pygame.mixer.Sound("Sons/Explosion.mp3"),
            'Feu' : pygame.mixer.Sound("Sons/Feu.mp3"),
            'Fin_jeu' : pygame.mixer.Sound("Sons/Fin_jeu.mp3"),
            'Fleche' : pygame.mixer.Sound("Sons/Fleche.mp3"),
            'Foudre' : pygame.mixer.Sound("Sons/Foudre.mp3"),
            'Foudre_v2' : pygame.mixer.Sound("Sons/Foudre_v2.mp3"),
            'Griffes' : pygame.mixer.Sound("Sons/Griffes.mp3"),
            'Laser' : pygame.mixer.Sound("Sons/Laser.mp3"),
            'Pistolet_silencieux' : pygame.mixer.Sound("Sons/Pistolet_silencieux.mp3"),
            'Projectile' : pygame.mixer.Sound("Sons/Projectile.mp3"),
            'Protection' : pygame.mixer.Sound("Sons/Protection.mp3"),
            'Revolver' : pygame.mixer.Sound("Sons/Revolver.mp3"),
            'Sabre' : pygame.mixer.Sound("Sons/Sabre.mp3"),
            'Soin' : pygame.mixer.Sound("Sons/Soin.mp3"),
            'Tir_1_coup' : pygame.mixer.Sound("Sons/Tir_1_coup.mp3"),
            'Tir_rafale' : pygame.mixer.Sound("Sons/Tir_rafale.mp3"),
            'Tir_rafale_v2': pygame.mixer.Sound("Sons/Tir_rafale_v2.mp3"),
            'Musique_lancement' : pygame.mixer.Sound("Sons/The_Avengers.mp3")
        }

    def bruit(self, name):
        if name in self.sounds:
            if name == 'Musique_lancement':
                self.sounds[name].play(-1)
            else :
                #self.sounds['Musique_lancement'].pause()
                self.sounds[name].play()
                #self.sounds['Musique_lancement'].unpause()
        else:
            print(f"Son {name} introuvable.")    