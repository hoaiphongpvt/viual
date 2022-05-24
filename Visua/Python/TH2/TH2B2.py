from cmath import sqrt
#ham kiem tra so nguyen to
def KTSNT(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0: count = count + 1
    if count == 2: return True

#ham kiem tra so doi xung
def SDN(n):
    kq = 0
    temp = 0
    while n != 0:
        temp = n % 10
        kq = (kq * 10) + temp
        n //= 10
    return kq

def KTSDX(n):
    sdn = SDN(n)
    if sdn == n: return True

#ham kiem tra so hoan chinh
def KTSHC(n):
    tong = 0
    for i in range (1,n):
        if n % i == 0:
            tong += i
    if tong == n: return True

#ham kiem tra so chinh phuong
def KTSCP(n):
    temp = sqrt(n)
    if temp**2 == n: return True

"""Viết chương trình nhập vào hai số M, N. In ra tất cả các số nguyên tố, số đối xứng, số hoàn chỉnh, số
chính phương trong khoảng [M,N] (nếu có)"""

M = int(input("Nhap so nguyen M: "))
N = int(input("Nhap so nguyen N: "))


print("Cac so nguyen to tu M den N la: ")
for i in range (M, N+1):
    kq = KTSNT(i)
    if kq == True: print(i)

print("Cac so doi xung tu M den N la: ")
for i in range (M, N+1):
    kq = KTSDX(i)
    if kq == True: print(i)

print("Cac so hoan chinh tu M den N la: ")
for i in range (M, N+1):
    kq = KTSHC(i)
    if kq == True: print(i)

print("Cac so chinh phuong tu M den N la: ")
for i in range (M, N+1):
    kq = KTSCP(i)
    if kq == True: print(i)