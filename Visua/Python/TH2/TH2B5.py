M = int(input("Nhap so nguyen M: "))

def KTSNT(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0: count = count + 1
    if count == 2: return True

print("%d so nguyen to dau tien la: " %M)
i = 1
while M != 0 :
    if KTSNT(i): 
        print(i)
        M = M - 1
    i = i + 1