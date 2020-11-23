import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

#if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
##   print(ability.name)
  #  print(ability.attack())