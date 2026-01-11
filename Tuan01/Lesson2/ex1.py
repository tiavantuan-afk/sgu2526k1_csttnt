#Tinh gia tri ham so
import math

# Nhap du lieu
x = float(input("Moi ban nhap vao gia tri cua bien so x: "))

# Xu ly
"""CAC BAN LAM BAI O DAY"""

#Tinh toan
tuso = math.sqrt(abs(x)) #Can bac 2 cua tri tuyet doi x
mauso = math.pow(x, 1.5) #x mu 3/2 (3/2 = 1.5)

#Tinh f(x)
#Dung factorial tinh giai thua
fx = x + (x**5 / math.factorial(5)) + (tuso/mauso)

#Xuat du lieu

print(f'Gia tri cua ham so f({x}) = {fx : .2f}.')
