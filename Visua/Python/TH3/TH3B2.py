from audioop import reverse
import re
from unittest import result

def dec2bin():
    result = ''
    p = 0
    x = int(input("Nhap so he 10: "))
    while x > 0: 
        result += str(x%2)
        x = int(x/2)
    return result


def bin2dec():
    x = input("Nhap so he 2: ")
    result = 0
    temp = str(x)
    somu = len(temp) - 1
    for i in range(0,len(temp)):
        result += int(temp[i]) * pow(2,somu)
        somu  -= 1
    return result

def hex2dec():
    x = input("Nhap so he 16: ")
    return hex(x)

a = bin2dec()
print(a)