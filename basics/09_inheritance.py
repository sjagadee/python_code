class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name}, my age is {self.age}")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name}, my age is {self.age}, and my color is {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")


c = Cat("raju", 5, "red")
c.show()
c.speak()

d = Dog("mana", 8)
d.show()
d.speak()