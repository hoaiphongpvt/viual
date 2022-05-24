class MyComplexNumber:
    def __init__(self, phanthuc, phanao):
        self.phanthuc = phanthuc
        self.phanao = phanao

    def __str__(self):
        return f"{self.phanthuc}+{self.phanao}j"
    
    def Input(self):
        print("Nhap phan thuc: ")
        self.phanthuc = input()
        print("Nhap phan ao: ")
        self.phanao = input()
    
    def my_addition(self, other):
        self.phanthuc += other.phanthuc
        self.phanao += other.phanao
    
    def my_subtract(self, other):
        self.phanthuc -= other.phanthuc
        self.phanao -= other.phanao
    
    def my_multi(self, other):
        self.phanthuc = self.phanthuc * other.phanthuc - self.phanao * other.phanao
        self.phanao = self.phanthuc * other.phanao + self.phanao * other.phanthuc

    def my_division(self, other):
        self.phanthuc = (self.phanthuc * other.phanthuc + self.phanao * other.phanao)/(other.phanthuc ** 2 + other.phanao ** 2)
        self.phanao = (self.phanao * other.phanthuc - self.phanthuc * other.phanao)/(other.phanthuc ** 2 + other.phanao ** 2)

    def __add__(self, other):
        self.my_addition(other)
    
    def __sub__(self, other):
        self.my_subtract(other)

    def __mul__(self, other):
        self.my_multi(other)

    def __truediv__(self, other):
        self.my_division(other)