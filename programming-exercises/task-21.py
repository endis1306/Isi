# Klasa bazowa Animal
class Animal:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        raise NotImplementedError("Metoda sound() musi być nadpisana w klasie dziedziczącej.")

    def __str__(self):
        return f"{self.name}, {self.age} lat, {self.sex}"


class Dog(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Hau!"

    def __str__(self):
        return f"{super().__str__()}, Rasa: {self.breed}"


class Cat(Animal):
    def __init__(self, name, age, sex, breed):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self):
        return "Miau!"

    def __str__(self):
        return f"{super().__str__()}, Rasa: {self.breed}"


class Fox(Animal):
    def __init__(self, name, age, sex):
        super().__init__(name, age, sex)

    def sound(self):
        return "Wa-wa!"

dog = Dog("Leon", 7, "Mężczyzna", "Owczarek niemiecki")
cat = Cat("Mruczek", 5, "Kobieta", "Pers")
fox = Fox("Kajtek", 8, "Mężczyzna")

print(dog)
print(dog.sound())

print(cat)
print(cat.sound())

print(fox)
print(fox.sound())

