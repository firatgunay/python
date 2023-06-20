# polymorphism

class Cherry():

    def __init__(self,name):
        self.name = name

    def info(self):
        return f"100 calories {self.name}"    

class Strawberry():

    def __init__(self,name):
        self.name = name

    def info(self):
        return f"150 calories {self.name}"    

cherry = Cherry("cherry")
strawberry = Strawberry("strawberry")

fruitList = [cherry,strawberry]

for fruit in fruitList:
    print(fruit.info())