x = int(input("Nhap 1 so nguyen: "))
sum = 0
count = 0

while x != 0:
    sum += x % 10
    count = count + 1
    x = int(x/10)

print("Tong cac chu so la: ̀%d" %sum)
print("Co %d chu so!" %count)