#Chuong trinh chuyen so giay do duoi dang so gio, so phut va so giay

# Nhập dữ liệu
t  = int(input('Nhap vao tong so giay: '))

# Xử lý
""" CÁC BẠN LÀM BÀI Ở ĐÂY """

#1h = 3600s, 1m = 60s

hh = t//3600
mm = (t%3600) // 60
ss = t % 60
# ...

# Xuất dữ liệu
print(f'{t} giay co dang {hh}:{mm}:{ss}')