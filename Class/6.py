#encapsulation

class Phone():

    def __init__(self,name,price):
        self.name = name
        self.__price = price # önüne __ alırsa değiştirelemez

    def info(self):
        print(f"{self.name} price is : {self.__price}")    


iPhone = Phone("İphone 14",500)

print(iPhone.info())

iPhone.price = 400
print(iPhone.info())    