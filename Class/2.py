class Person():
    #property (aşağıda belirtmeye gerek yok)
    #name = ""
    #age = 0
    #gender = ""

    #initilazier method 
    
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    

p2 = Person("p2", 35, "male")

print(p2.name)
print(p2.age)
print(p2.gender)