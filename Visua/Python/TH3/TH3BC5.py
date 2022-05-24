from stringprep import map_table_b2


myString = input('Nhap vao chuoi cua ban: ')

countUpper = 0
countLower = 0

for i in range(0,len(myString)):
    if myString[i].islower():
        countLower += 1
    elif myString[i].isupper():
        countUpper += 1

print('So luong chu thuong trong chuoi la: ', countLower)
print('So luong chu hoa trong chuoi la: ', countUpper)