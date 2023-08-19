# ex 2.4.2


class BigThing:
    def __init__(self, var):
        self.var = var

    def size(self):
        if isinstance(self.var, int):
            return self.var
        if isinstance(self.var, dict) or isinstance(self.var, list) or isinstance(self.var, str):
            return len(self.var)


class BigCat(BigThing):
    def __init__(self, var, weight):
        BigThing.__init__(self, var)
        self.weight = weight
        self.name = var

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())

    cutie = BigCat("mitzy", 22)
    print(cutie.size())

    cat2 = BigCat("mikey", 16)
    print(cat2.size())

    cat2 = BigCat("mikey", 1)
    print(cat2.size())


if __name__ == "__main__":
    main()
