L = [2, 4, 9, 3, 5]

#Thay the phan tu dau thanh so am tuong ung
L[0] = L[0] * (-1)

#Them 20 vao cuoi danh sach
L.append(20)

#Them so 0 vao vi tri thu 3 trong danh sach
L.insert(3, 0)

#Xoa phan tu tại vi tri so 4 trong danh sach
L.pop(4)

#Them list [0, 0, 0] vao sau danh sach tren
L = L + [0, 0, 0]

#Sap xep dánh sach giam dan
L.sort(reverse=True)



print(L)