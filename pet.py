# pet.py

class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating... 🍖")

    def sleep(self):
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping... 😴")

    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing... 🎾")
        else:
            print(f"{self.name} is too tired to play. 😔")

    def train(self, trick):
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}! 🎉")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows these tricks: {', '.join(self.tricks)} 🐾")
        else:
            print(f"{self.name} doesn't know any tricks yet.")

    def get_status(self):
        print(f"📋 {self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")


# 🐱 Cat subclass with extras
class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)
        self.purring = True
        self.favorite_spot = "sunbeam"

    def purr(self):
        if self.happiness > 5:
            print(f"{self.name} is purring contentedly... 🐱💤")
        else:
            print(f"{self.name} doesn’t feel like purring right now.")

    def scratch_furniture(self):
        print(f"{self.name} is scratching the furniture! 😼")
        self.happiness += 1
        self.energy -= 1

    def nap_in_sun(self):
        print(f"{self.name} is napping in a {self.favorite_spot}... ☀️")
        self.energy = min(10, self.energy + 3)
        self.happiness = min(10, self.happiness + 2)
