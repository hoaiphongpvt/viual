from ctypes.wintypes import PINT


n = int(input("Nhap vao so nguyen n: "))

temp = 0
kq = 0
while n != 0:
    temp = n % 10
    kq = (kq * 10) + temp
    n //= 10

result = reversed(str(kq))

for i in result:
    print(i)