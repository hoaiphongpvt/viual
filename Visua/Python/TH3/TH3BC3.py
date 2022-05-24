from ast import MatchStar
from tokenize import Number
from traceback import print_tb


myString = input('Nhap vao mot chuoi: ')

temp = []

for i in myString:
    if i not in temp:
        if i == ' ': 
            continue
        temp += i

print(temp)

for i in temp:
    count = 0
    for j in range(0,len(myString)):
        if i == myString[j]:
            count += 1
    print('So lan xuat hien cua ki tu ' + i + ' la: ' + str(count) + ' lan!')