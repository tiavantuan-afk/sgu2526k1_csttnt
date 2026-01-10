import math

# Nhập bán kính là số thực
r = float(input("Nhập bán kính hình tròn (số thực): "))

# Tính chu vi: cv = 2πr
chu_vi = 2 * math.pi * r

# Tính diện tích: dt = πr²
dien_tich = math.pi * r * r

# In kết quả
print(f"Bán kính: {r}")
print(f"Chu vi hình tròn: {chu_vi:.2f}")
print(f"Diện tích hình tròn: {dien_tich:.2f}")