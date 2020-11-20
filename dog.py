#dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("Dog initialized!")

    def bark(self):
        print("Woof!")

    def sit(self):
        print((self.name)+' sits')

    def rollover(self):
        print((self.name)+' rolls over')

