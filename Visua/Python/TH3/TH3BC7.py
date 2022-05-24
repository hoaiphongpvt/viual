from ast import Delete
import string
from traceback import print_tb

myString = input('Nhap vao chuoi cua ban: ').split(' ') #ham split de tac cac phan tu voi nhau qua dau khoang cach

print(myString)

for i in set(myString): #su dung ham set de loc cac phan tu trung
    count = 0
    for j in range(len(myString)):
        if i == myString[j]:
            count += 1
    print("So la xuat hien cua tu "+ i + ' la ', count)