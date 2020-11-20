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
        return total_damage

    def defend(self, damage_amt):
        #Calculate the total amount blocked from all armor blocks
        total_block = 0
        for armor in self.armor:
            #add the total armor score to block
            total_block += armor.defend()
        #return total damage mitigated
        return total_block

    def take_damage(self, damage):
        #Updates self.current_health to reflect damage taken
        #Minus the amount returned from calling self.defend(damage)
        self.current_health -= damage - self.defend(damage)

    def fight(self, opponent):
        #Randomly choses between the selected hero and opponent as winner
        hero_choice = [self.name, opponent.name]
        #Returns winner
        print(f'{random.choice(hero_choice)} wins!')
        

if __name__ == "__main__":
    my_hero = Hero('Grace Hopper',200)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("King")
    hero2 = Hero("Queen")
    ability = ("Shmoove", 25)
    ability2 = ("Ice", 15)
    shield = Armor("Shield", 50)
    my_hero.add_armor(shield)
    my_hero.take_damage(50)
    print(hero.current_health)
    #hero1.fight(hero2)