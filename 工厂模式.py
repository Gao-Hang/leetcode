class Person:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight


class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)


class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)


class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("ll", "F")