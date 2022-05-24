"""Viết chương trình nhập vào một số nguyên n. Kiểm tra xem số đó có phải là số nguyên tố, số đối xứng, 
số hoàn chỉnh, số chính phương hay không?"""
from cmath import sqrt


n = int(input("Nhap vao so nguyen n: "))

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

result = KTSCP(n)
if result == True:
    print("%d la so chinh phuong!" %n)
else:
    print("%d khong phai la so chinh phuong!" %n)    