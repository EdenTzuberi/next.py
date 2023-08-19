# ex 2.5

class Animal:
    """
    A class used to represent an animal.
     """
    def __init__(self, name="None", hunger=0):
        self.zoo_name = "Hayaton"
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """
        The function returns animal name.
        """
        return self._name

    def talk(self):
        """
        The function will make the animal talk.
        """
        pass

    def is_hungry(self):
        """
        The function checks if the animal is hungry or not, and returns True if it is and False if it is not.
        """
        if self._hunger > 0:
            return True
        else:
            return False

    def feed(self):
        """
        The function will "feed" the animal by decreasing the hunger value by one.
        """
        self._hunger -= 1


class Dog(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def talk(self):
        """
        The function will make the dog talk.
        """
        print("woof woof")

    def fetch_stick(self):
        """
        The function will make the dog fetch a stick.
        """
        print("There you go, sir!\n")


class Cat(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def talk(self):
        """
        The function will make the cat talk.
        """
        print("meow")

    def chase_laser(self):
        """
        The function will make the cat chase laser.
        """
        print("Meeeeow\n")


class Skunk(Animal):
    def __init__(self, name, hunger, stink_count=6):
        Animal.__init__(self, name, hunger)
        self._stink_count = stink_count

    def talk(self):
        """
        The function will make the skunk talk.
        """
        print("tsssss")

    def stink(self):
        """
        The function will make the skunk stink.
        """
        print("Dear lord!\n")


class Unicorn(Animal):
    def __init__(self, name, hunger):
        Animal.__init__(self, name, hunger)

    def talk(self):
        """
        The function will make the unicorn talk.
        """
        print("Good day, darling")

    def sing(self):
        """
        The function will make the unicorn sing.
        """
        print("I’m not your toy...\n")


class Dragon(Animal):
    def __init__(self, name, hunger, color="Green"):
        Animal.__init__(self, name, hunger)
        self._color = color

    def talk(self):
        """
        The function will make the dragon talk.
        """
        print("Raaaawr")

    def breath_fire(self):
        """
        The function will make the dragon breath fire.
        """
        print("$@#$#@$\n")


def main():
    # The animals of the zoo
    dog1 = Dog("Brownie", 10)
    cat1 = Cat("Zelda", 3)
    skunk1 = Skunk("Stinky", 0)
    unicorn1 = Unicorn("Keith", 7)
    dragon1 = Dragon("Lizzy", 1450)
    dog2 = Dog("Doggo", 80)
    cat2 = Cat("Kitty", 80)
    skunk2 = Skunk("Stinky Jr.", 80)
    unicorn2 = Unicorn("Clair", 80)
    dragon2 = Dragon("McFly", 80)

    # List of the zoo animals
    zoo_lst = [dog1, cat1, skunk1, unicorn1, dragon1, dog2, cat2, skunk2, unicorn2, dragon2]

    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__, animal.get_name())
            animal.talk()

        while animal.is_hungry():
            animal.feed()

        # Special methods
        if isinstance(animal, Dog):
            Dog.fetch_stick(animal)
        elif isinstance(animal, Cat):
            Cat.chase_laser(animal)
        elif isinstance(animal, Skunk):
            Skunk.stink(animal)
        elif isinstance(animal, Unicorn):
            Unicorn.sing(animal)
        else:
            Dragon.breath_fire(animal)

        # Print zoo name
    print("zoo name:\t", dog1.zoo_name)


if __name__ == "__main__":
    main()
