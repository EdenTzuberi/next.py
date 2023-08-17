# Object Oriented Programming - 2.4

class Animal:
    def __init__(self, name):
        self._name = name
        self._hunger = 0
        self._fun = 0

    def play(self):
        self._fun += 1

    def eat(self):
        if self._hunger > 0:
            self._hunger -= 1

    def go_to_toilet(self):
        self._hunger += 1


class Dog(Animal):
    def __init__(self, name, fur_color):
        Animal.__init__(self, name)
        self._fur_color = fur_color

    def go_for_walk(self):
        self._fun += 2
        print("Waff waff! My fun level is rising, and its: ", self._fun)

    def eat(self):
        super().eat()
        print("eating a bone!")

    def __str__(self):
        return "My name is {} and I'm a dog!".format(self._name)


def main():
    fluppy = Dog("Fluppy", "Brown")
    fluppy.play()
    fluppy.eat()
    fluppy.go_for_walk()
    print(str(fluppy))


if __name__ == "__main__":
    main()

