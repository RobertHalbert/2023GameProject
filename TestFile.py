class Object1:
    item1 = False
    def Function1(item2):
        if item2 == False:
            print("False")

class Object2(Object1):
    def __init__(self,item2) -> None:
        self.item2 = item2
        super().__init__()
    item2 = True
    def object2function(self):
        Object1.Function1(self)

Object2.object2function(Object2.item1)