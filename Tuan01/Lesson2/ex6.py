import math
# Nhập dữ liệu
n   = int(input("Moi ban nhap so nguyen n: "))

# Xử lý 
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
if n < 2:
    lant = False # Dkien be hon thi khong phai
else:
    lant = True
    #Duyet tu 2 den can bac 2 cua n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: 
            lant = False #Neu chia het cho i thi khong phai so nguyen to
            break
# ...

# Xuất dữ liệu
if lant == True:
    print(f'{n} la so nguyen to.')
else:
    print(f'{n} khong la so nguyen to.')