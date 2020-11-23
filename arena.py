from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
from random import choice

class Arena:
    #Arena class

    def __init__(self):
        #instantiate properties
        self.team_one = team_one
        self.team_two = team_two
        self.previous_winner = None

    def create_ability(self):
        #prompty used for ability information
        name = ""
        while len(name) < 1:
            name = input("What is the ability name?  ")
        max_damage = 0
        while max_damage < 1:
            max_damage = input("What is the max damage of the ability?  ")
            try:
                max_damage = int(max_damage)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_damage = 0
                print("Please enter a number.")
        return Ability(name, max_damage)

    def create_armor(self):
        #prompt used for armor information
        name = ""
        while len(name) < 1:
            name = input("What is the armor name?  ")
        max_block = 0
        while max_block < 1:
            max_block = input("What is the max block of the armor?  ")
            try:
                max_block = int(max_block)
                print(f"{name} has been added.")
                break
            except(ValueError, TypeError):
                max_block = 0
                print("Please enter a number.")
        return Armor(name, max_block)

    def create_hero(self):
        #Prompt user for Hero information.
        #Return Hero with values from user input.
        print("\n")
        hero_name = ""
        while len(hero_name) < 1:
            hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input(
                "\n[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: "
            )
            if add_item == "1":
                abilty = self.create_ability()
                hero.add_ability(abilty)
            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero

    def build_team_one(self):
        #Prompt user to build team 1
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        #Prompt user to build team 2
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self, team_one, team_two):
        team_one.attack(team_two)

    def show_stats(self, team_one, team_two):
       #Print team statistics to terminal
        print("\n")
        print("{:-^50}".format("STATS"))
        print("\n")
        print(f"{team_one.name} statistics: ".upper())
        team_one_survival_count = self.surviving_heroes(team_one)
        self.kd_average(team_one)
        print("\n")
        print(f"{team_two.name} statistics: ".upper())
        team_two_survival_count = self.surviving_heroes(team_two)
        self.kd_average(team_two)
        print("\n")
        self.winning_team(team_one, team_one_survival_count, team_two, team_two_survival_count)
        print("\n")

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()