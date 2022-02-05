class Prey:

    def flee(self):
        print("This animal flees!")


class Predator:

    def hunt(self):
        print("This animal hunts!")


class Fish(Prey, Predator):

    def swim(self):
        print("This fish is swimming!")


fish = Fish()
fish.flee()
fish.hunt()
fish.swim()
