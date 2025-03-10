class Dog:
    name='Alex'
    age=1
    coat_color='czarny'
    def __init__(self, name=name, age=age, coat_color=coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    def sound(self):
        print(f"{self.name} is barking!")


Dog1 = Dog()
Dog1.sound()

Dog2 = Dog('Pawel', 5, 'biały')
Dog2.sound()

Dog3 = Dog('Leon', 7, 'broązowy')
Dog3.sound()
