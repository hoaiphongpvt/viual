def KTSNT(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0: count = count + 1
    if count == 2: return True

N = int(input("Nhap so nguyen N: "))

print("Cac so nguyen to nho hon N la: ")

for i in range (1, N):
    if KTSNT(i): print(i)