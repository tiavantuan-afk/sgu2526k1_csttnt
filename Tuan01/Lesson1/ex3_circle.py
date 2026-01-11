import math

# Nhập bán kính là số thực
r = float(input("Nhập bán kính hình tròn (số thực): "))

# Tính chu vi
chu_vi = 2 * math.pi * r

# Tính diện tích
dien_tich = math.pi * r * r

# Int kết quả
print(f"Bán kính: {r}")
print(f"Chu vi hình tròn: {chu_vi:.2f}")
print(f"Diện tích hình tròn: {dien_tich:.2f}")