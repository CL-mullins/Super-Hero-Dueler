import random
from ability import Ability
from armor import Armor

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armor = list()

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage +=ability.attack()
        return total_damage

    def fight(self, opponent):
        hero_choice = [self.name, opponent.name]
        #difficulties trying to choose between the opponent and the mentioned hero
        print(f'{random.choice(hero_choice)} wins!')
        

if __name__ == "__main__":
    my_hero = Hero('Grace Hopper',200)
    print(my_hero.name)
    print(my_hero.current_health)
    hero1 = Hero("King")
    hero2 = Hero("Queen")
    ability = ("Shmoove", 25)
    ability2 = ("Ice", 15)
    my_hero.add_ability(ability)
    my_hero.add_ability(ability2)
    print(my_hero.abilities)
    print(my_hero.attack)
    #hero1.fight(hero2)