class Person:
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def addFive(val):
        return val + 5

print(Person.addFive(6))