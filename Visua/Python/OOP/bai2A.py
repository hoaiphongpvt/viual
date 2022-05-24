class Shape:
    def __init__(self):
        pass
    def getArea(self):
        return 0
    class Square:
        def __init__(self,length):
            self.length = length
        def getArea(self):
            return self.length * self.length

myShape = Shape.Square(10)

print(myShape.getArea())