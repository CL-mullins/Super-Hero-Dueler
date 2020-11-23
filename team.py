from random import choice
#import choice


class Team:
    
    def __init__(self, name):
        #initialize a team with an empty list of heros
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        #Remove a hero from the list, if hero isn't found, return 0
        foundHero = False
        #loop through each hero in our list
        for hero in self.heroes:
        # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
            # set our indicator to True
                foundHero = True
        # if we looped through our list and did not find our hero,
        # the indicator would have never changed, so return 0
        if not foundHero:
            return 0
