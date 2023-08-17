# ex 2.2.2


class Cat:
    cats_num = 0

    def __init__(self, name="Octavio", age=0):
        self._cats_name = name
        self._age = age
        Cat.cats_num += 1

    def set_name(self, new_name):
        self._cats_name = new_name

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._cats_name


def main():
    cat1 = Cat("Mike", 3)
    cat2 = Cat("Mitzi", 2)
    cat3 = Cat()

    cat1.birthday()
    cat2.birthday()

    print("Cat 1:\t age:", cat1.get_age())
    print("Cat 2:\t age:", cat2.get_age())
    print("Cat 3:\t age:", cat3.get_age())
    print("Number of cats in the class:", Cat.cats_num)

    print(cat1.get_name())
    print(cat2.get_name())
    print(cat3.get_name())

    cat1.set_name("Tesi")
    print(cat1.get_name())

if __name__ == "__main__":
    main()
