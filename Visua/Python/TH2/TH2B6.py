print("Cac so chia het cho 7 nhung khong chia het cho 5 tu 99 den 999 la:")

for i in range(99,999 + 1):
    if ((i % 7 == 0) & (i % 5 != 0)): 
        print(i)