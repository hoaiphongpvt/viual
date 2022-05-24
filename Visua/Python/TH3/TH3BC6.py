
def KTSNT(n):
    count = 0
    for i in range (1,n+1):
        if n % i == 0: count += 1
    if count == 2: return True
    return False

myString = input('Nhap vao chuoi cac so nguyen va cach 1 dau , : ' ).split(',')


for i in myString:
    if KTSNT(int(i)):
        print(i)