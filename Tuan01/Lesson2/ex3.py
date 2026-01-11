# Nhập dữ liệu
a  = int(input('Moi ban nhap he so a: '))
b  = int(input('Moi ban nhap he so b: '))

# Xử lý
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
if a == 0:
    if b == 0:
            flag = -1 
    else:
            flag = 0
else:
    flag = 1
    x = -b / a 
# ...
    
# Xuất dữ liệu
s = f'Phuong trinh {a}x + {b} = 0'
if flag == -1:
    print(f'{s} vo so nghiem.')
elif flag == 0:
    print(f'{s} vo nghiem.')
else:
    print(f'{s} co 1 nghiem x = {x: .2f}.')
# if