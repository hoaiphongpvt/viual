def bin2dec(x):
    result = 0
    temp = str(x)
    somu = len(temp) - 1
    for i in range(0,len(temp)):
        result += int(temp[i]) * pow(2,somu)
        somu  -= 1
    return result


myNumber = (input("Nhap chuoi so he nhi phan: ")).split(',')

print(myNumber)

for i in myNumber:
    print(bin2dec(int(i)))
