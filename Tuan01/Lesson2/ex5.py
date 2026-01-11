# Nhập dữ liệu
n   = int(input("Moi ban nhap so nguyen n: "))

# Xuất dữ liệu
s   = 0
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
#Cho chay vong lap
for i in range(1, n + 1):
    if i % 2 == 0: #Neu chia het cho 2 la so chan
        s += i
# ...

print(f'Tong cac so chan tu 1 den {n} la {s}.')