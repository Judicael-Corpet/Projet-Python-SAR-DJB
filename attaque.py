
import random
import pygame
class Attaque:
    def __init__(self, name, attack_power, quantite, distance_attack, precision, offsets):
        self.name = name
        self.attack_power = attack_power
        self.quantite = quantite
        self.distance_attack = distance_attack
        self.precision = precision
        self.offsets = offsets

    def utiliser(self, cible):
        if self.quantite > 0:
            damage = self.attack_power * self.precision * (cible.defense / 100) * (1 / self.distance_attack)
            cible.take_damage(damage)
            self.quantite -= 1
            return damage
        else:
            print(f"{self.name} n'a plus de munitions.")
            return 0
        
        
    def attack(self, type_attack, target):
        
        
        
        """Attaque une unité cible."""
        
        print ("le type de cet objet est :")
 
    
        if type_attack == "Aucune Action" :
            self.attaque_selectionne = aucune_action
        
        elif type_attack == "Poings" :
            self.attaque_selectionne = poings
        
        elif type_attack == "Griffes" :
            self.attaque_selectionne = griffes

        elif type_attack == "Lancer_bouclier" :
            self.attaque_selectionne = lancer_bouclier

        elif type_attack == "Casser_les_murs" :
            self.attaque_selectionne = casser_les_murs
        
        elif type_attack == "Laser" :
            self.attaque_selectionne = laser
        
        elif type_attack == "Missile":
            self.attaque_selectionne = missile
        
        elif type_attack == "Bloquer_adversaire":
            self.attaque_selectionne = bloquer_adversaire

        elif type_attack == "Attaque_toile":
            self.attaque_selectionne = attaque_toile
        
        elif type_attack == "Marteau":
            self.attaque_selectionne = marteau
        
        elif type_attack == "Foudre":
            self.attaque_selectionne = foudre
        
        elif type_attack == "Attaque_branche":
            self.attaque_selectionne = attaque_branche
        
        elif type_attack == "Protection":
            self.attaque_selectionne = protection
        
        elif type_attack == "Pistolets":
            self.attaque_selectionne = pistolets
        
        elif type_attack == "Fleche_Yaka":
            self.attaque_selectionne = fleche_yaka

        elif type_attack == "Boule_de_feu":
            self.attaque_selectionne = boule_de_feu

        elif type_attack == "Soigner":
            self.attaque_selectionne = soigner

        elif type_attack == "Projectile":
            self.attaque_selectionne = projectile
        
        # print (f"Lattaque selectionnee pour la methode attack {self.attaque_selectionne.name}")
        for red_x, red_y in self.red_cases :
            if target.x == red_x and  target.y == red_y :
                target.health = target.health - self.attaque_selectionne.attack_power # ICI SIMPLE APRES ON POURRA METTRE LA PRECISION? LA DEFENSE EN JEUX
     
    
    def draw_attack_menu(self) :
        """Dessine le menu des attaques."""
        #Fond noir dans le coin inférieur gauche
        pygame.draw.rect(self.screen, (0, 0, 0), (20, 340, 250, 150 ))
        pygame.draw.rect(self.screen, (255, 255, 255), (20, 340, 250, 150), 2)  # Bordure blanche

        list_attacks = self.attaques
        # Dessiner chaque attaque dans le rectangle
        for i, attaque in enumerate(list_attacks):
            color = (0, 255, 0) if i == self.selected_attack_index else (255, 255, 255)  # Mettre en surbrillance l'attaque sélectionnée
            text = pygame.font.Font(None, 36).render(attaque, True, color)
            self.screen.blit(text, (30, 350 + i * 30))  # Positionnement des attaques
        


# Instantacions des attaques

aucune_action=Attaque(
    name="Aucune_attaque",
    attack_power=0,
    quantite=10000,
    distance_attack=0,
    precision=random.uniform(0, 0),
    offsets=[(0, 0)]    
    
)

poings = Attaque(
    name="Poings",
    attack_power=70,
    quantite=100,
    distance_attack=1,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

griffes = Attaque(
    name="Griffes",
    attack_power=90,
    quantite=3,
    distance_attack=3,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

lancer_bouclier = Attaque(
    name="Lancer_bouclier",
    attack_power=90,
    quantite=3,
    distance_attack=3,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

casser_les_murs = Attaque(
    name="Casser_les_murs",
    attack_power=100,
    quantite=1,
    distance_attack=1,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

laser = Attaque(
    name="Laser",
    attack_power=100,
    quantite=1,
    distance_attack=5,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

missile = Attaque(
    name="Missile",
    attack_power=130,
    quantite=1,
    distance_attack=6,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

bloquer_adversaire = Attaque(
    name="Bloquer_adversaire",
    attack_power=100,
    quantite=2,
    distance_attack=4,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

attaque_toile = Attaque(
    name="Attaque_toile",
    attack_power=90,
    quantite=3,
    distance_attack=3,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

marteau = Attaque(
    name="Marteau",
    attack_power=130,
    quantite=2,
    distance_attack=5,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

foudre = Attaque(
    name="Foudre",
    attack_power=150,
    quantite=1,
    distance_attack=6,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

attaque_branche = Attaque(
    name="Attaque_branche",
    attack_power=100,
    quantite=100,
    distance_attack=3,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

protection = Attaque(
    name="Protection",
    attack_power=150,
    quantite=1,
    distance_attack=1,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

pistolets = Attaque(
    name="Pistolets",
    attack_power=120,
    quantite=10,
    distance_attack=4,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

fleche_yaka = Attaque(
    name="Fleche_Yaka",
    attack_power=150,
    quantite=3,
    distance_attack=5,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

boule_de_feu = Attaque(
    name="Boule_de_feu",
    attack_power=150,
    quantite=3,
    distance_attack=5,
    precision=random.uniform(0.5, 1),
    offsets=[(-5, 0), (5, 0), (0, -5), (0, 5)]
)

soigner = Attaque(
    name="Soigner",
    attack_power=0,  # Soins, pas d'attaque
    quantite=3,
    distance_attack=1,
    precision=1,
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)

projectile = Attaque(
    name="Projectile",
    attack_power=100,
    quantite=3,
    distance_attack=5,
    precision=random.uniform(0.5, 1),
    offsets=[(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
)
