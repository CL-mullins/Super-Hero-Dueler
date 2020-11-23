import random
from ability import Ability
from armor import Armor
#Class for a super hero with abilities, attack and armor
class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        #Add armor to self.armor
        #Adds armor object that is passed into self.armors
        self.armor.append(armor)

    def attack(self):
        #start our total out at 0
        total_damage = 0
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
            #return the total damage    
            return int(total_damage)

    def defend(self, damage_amt):
        #Calculate the total amount blocked from all armor blocks
        total_block = 0
        for armor in self.armor:
            #add the total armor score to block
            total_block += armor.block()
            #TODO: Fix error here
        #return total damage mitigated
        return total_block

    def take_damage(self, damage):
        #Updates self.current_health to reflect damage taken
        #Minus the amount returned from calling self.defend(damage)
        self.current_health -= (damage + self.defend(damage))

    def fight(self, opponent):
        #hero_choice = [self, opponent]
        #Check to see if hero has abilities, if no abilities, print draw
        if len(self.abilities) > 0 or len(opponent.abilities) > 0:
            while(self.is_alive() and opponent.is_alive()):
                #Start fighting loop until a hero has won
                print(f'{opponent.name} attacked {self.name}!')
                self.take_damage(opponent.attack())
                print(f"{self.name}'s remaining health: {self.current_health}")
                print(f'{self.name} attacked {opponent.name}!')
                opponent.take_damage(self.attack())
                print(f"{opponent.name}'s remaining health: {opponent.current_health}")

            if not self.is_alive():
                print(f"\n{self.name} has been defeated by {opponent.name}\n".upper())
            elif not opponent.is_alive():
                print(f"\n{opponent.name} has been defeated by {self.name}\n".upper())
        else:
            print("Draw!")
        #print(f'{random.choice(hero_choice)} wins!')

    def is_alive(self):
        #checks to see if the hero is still alive
        if self.current_health <= 0:
            return False
        else:
            return True
        

if __name__ == "__main__":
    my_hero = Hero('Grace Hopper',200)
    hero1 = Hero('Dumbledore',200)
    ability = Ability("Shmoove", 25)
    ability2 = Ability("Ice", 15)
    ability3 = Ability("Laugh", 30)
    shield = Armor("Shield", 50)
    my_hero.add_ability(ability)
    hero1.add_ability(ability2)
    my_hero.add_ability(ability3)
    my_hero.add_armor(shield)
    my_hero.fight(hero1)
    #hero1.fight(hero2)