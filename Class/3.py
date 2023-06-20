class Dog():
    year = 7

    def __init__(self,age):
        self.age = age
        self.DoghumanAge = age * self.year #aşağıdaki gibi de yapılabilir
     
    def humanAge(self):
        return self.age * Dog.year #Dog.year == self.year   


myDog = Dog(3)
print(myDog.DoghumanAge)
print(myDog.humanAge())