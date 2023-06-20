# inheritance (kalıtım alma)

class Musician():

    def __init__(self,name):
        self.name = name
        print("musician class");
    
    def test1(self):
        print("test 1")

    def test2(self):
        print("teat 2")    


class MusicianPlus(Musician):

    def __init__(self,name):
        Musician.__init__(self,name)
        print("musician plus")

atlas = MusicianPlus("atlas")

print(atlas.name)
print(atlas.test1)
print(atlas.test2)


