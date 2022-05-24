from audioop import avg
import numbers
from traceback import print_tb


class Student:
    def __init__(self,name,number):
        self.name = name
        self.number = number
        self.score = [0] * number
    
    def getName(self):
        return self.name

    def getScore(self,i):
        return self.score[i]

    def inputScore(self):
        for i in range(self.number):
            self.score[i] = float(input(f"Nhap diem mon thu {i} :"))
    
    def getAversge(self):
        return sum(self.score)/self.number

    def getHightScore(self):
        return max(self.score)
    
    def HocBong(self):
        if self.getAversge() >= 8.0:
            for i in self.score:
                if(i < 4):
                    return False
            return True
        return False
    def __str__(self) -> str:
        return "Name: {}, Score: {}, Diem Trung Binh: {}, Hoc Bong: {}".format(self.name, self.score, self.getAversge(), self.HocBong())


s1 = Student("Phong", 4)

s1.inputScore()

print(s1)
