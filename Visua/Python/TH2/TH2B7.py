M = int(input("Nhap so nguyen M: "))
N = int(input("Nhap so nguyen N: "))

for i in range(M,N+1):
    if((i % 9 == 0) & (i % 7 == 0)):
        print(i) 
        break