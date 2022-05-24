from traceback import print_tb


a = int(input("Nhap so nguyen a: "))
b = int(input("Nhap so nguyen b: "))

def UCLN(a,b):
    while a != b: 
        if a > b : a = a - b
        else: b = b - a
    return a

result = UCLN(a,b)

print("Uoc chung lon nhat la: %d" %result)

def BCNN(a,b):
    return (a*b)/UCLN(a,b)

result2 = BCNN(a,b)

print("Boi chung nho nhat la: %d" %result2)

#su dung de quy

