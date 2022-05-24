"""#Giả sử từ điển d = {'b':200, 'a':100, 'c':1}. Thực hiện các câu lệnh theo yêu cầu sau:

d = {'b':200, 'a':100, 'c':1}

#Thay thế giá trị khóa b thành số âm tương ứng
d['b'] = d['b'] * (-1)

#Thêm một khóa 'e' có giá trị là 500
d['e'] = 500

# Xóa khóa b ra khỏi từ điển theo cách an toàn
del(d['b'])

#In ra các cặp (key,value) ra màn hình theo thứ tự từ điển
for key in d:
    print(key, d[key])
"""

#Tạo một tập hợp gồm các phần từ từ 0 đến 200. In tập hợp ra màn hình

"""mySet = set()

for i in range(201):
    mySet.add(i)

print(mySet)"""

#Tạo một tập hợp gồm các số nguyên tố từ 10 đến 200.In ra màn hình
def checkSnt(n):
    count = 0
    i = 1
    for i in range(1,n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

mySet = set()

for i in range(2001):
    if checkSnt(i):
        mySet.add(i)

print(mySet)