from ability import Ability
from random import randint

class Weapon(Ability):
    def attack(self):
        #return a random integer between 1/2 of the weapon's max damage and it's full max damage
        return randint((self.max_damage // 2), self.max_damage)
