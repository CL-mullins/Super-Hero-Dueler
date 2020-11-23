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
        self.team_one = Team("One")
        self.team_two = Team("Two")
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
        return self.team_one

    def build_team_two(self):
        #Prompt user to build team 2
        team_two = Team("Team Two")
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def surviving_heroes(self, team):
        #Return the survival count for a given team
        survival_count = 0
        for hero in team.heroes:
            if hero.is_alive():
                print(f"{hero.name} survived")
                survival_count += 1
        if not survival_count:
            print("no heroes survived")
        return survival_count

    def kd_average(self, team):
        #Prints kill/death average for given team
        team_kills = 0
        team_deaths = 0
        for hero in team.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(f"average K/D: {team_kills/team_deaths}")

    def winning_team(self, team_one, team_one_survival_count, team_two, team_two_survival_count):
        #Prints winning team for two given survival counts
        if team_one_survival_count and team_two_survival_count:
            print("{:=^50}".format("No winner could be declared").upper())
            self.previous_winner = None
        elif team_one_survival_count:
            p = f"{team_one.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = team_one
        else:
            p = f"{team_two.name} won"
            print("{:=^50}".format(p).upper())
            self.previous_winner = team_two

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

    #Instantiate Team
    team_one = Team("Team 1")
    team_two = Team("Team 2")

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle(team_one, team_two)
        arena.show_stats(team_one, team_two)
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()