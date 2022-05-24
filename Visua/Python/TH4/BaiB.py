from operator import index, indexOf
import re
from xml.dom.minidom import Element


#A = ['3', '27', '5', '123', '9', '1']

#Viet ham sap xep chuoi tang dan theo hai kieu 
"""A.sort() #String comepare
A.sort(key=int) #Integer comepare
"""
"""Viet chuong trinh in ra list sau khi da xoa so
tai vi tri thu 1, thu 2 va thu 3 thu 6 trong
[12, 24, 35, 70, 88, 120, 155]"""
l = [12, 24, 35, 70, 88, 120, 155]
indexdel = [1,2,3,6]
L = [x for i,x in enumerate(l) if i not in indexdel]
print(L)
#Xoa cac phan tu trung nhau trong list
#Dung vong lap, yeu cau khong dung ham cua kieu du lieu dictionary va set.
"""A = [1, 2, 3, 1, 2, 5, 6, 7, 8]
temp = []
for i in A:
    if i not in temp:
        temp.append(i)
#Khong rang buoc
temp2 = []
for i in set(A):
    temp2.append(i)
print(temp2)"""

#Dem so lan xuat hien cua cac phan tu trong list

"""A = [1,1,1,1,2,2,2,2,3,3,4,5,5]

Temp = []

for i in A:
    if i not in Temp:
        Temp.append(i)

for i in Temp:
    count = 0
    for j in A:
        if i == j:
            count += 1
    print("So lan xuat hien cua ", i ," la ", count, " lan")

#Khong rang buoc
for i in Temp:
    print(A.count(i))"""


#Viet chuong trinh nhap vao mot list chua cac so nguyen duong theo cac yeu cau sau
#Nhap truoc so phan tu cua list, sau do nhap tung phan tu

"""myList = []
n = int(input("Nhap vao so phan tu cua mang: "))
for i in range(n):
    print("Nhap phan tu thu ", i, ": ")
    myList.append(int(input()))

print(myList)

#Khong nhap truoc so luong phan tu, qua trinh nhap ket thuc neu nhap vao -1


while (True):
    n = int(input())
    if n == (-1):
        break
    else: myList.append(n) 

print(myList)"""


"""Cho 2 list như sau: ( 2 list có thể khác độ dài)
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
Viết chương trình tạo ra một list chứa các phần tử chung của 2 list ban đầu theo các yêu cầu sau:
a) Không dùng List Comprehension
b) Dùng List Comprehension"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""myList = []
for i in a:
    if i in b:
        myList.append(i)
"""

"""newList = [x for x in a if x in b]

print(set(newList))
"""

