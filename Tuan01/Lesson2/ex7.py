import math

def NhapDuLieu():
    """
    Input: 
        Ban phim = 1 5 6
    Output:
        (a, b, c) --> (1, 5, 6)
    """
    while True:
        try:
            data = input("Moi ban nhap he so a, b, c: ")
            a, b, c = map(float, data.split())
            return a, b, c
        except:
            print("Ban nhap sai! Moi ban nhap lai!")


def GiaiPhuongTrinhBac2(a, b, c):
    """
    Input: a, b, c
    Output: 
    + flag = -1 (VSN), 0 (VN), k (k nghiem)
    + () --> flag = -1, 0
    + (x) --> flag = 1
    + (x1, x2) --> flag = 2
    """
    import math
    flag = None
    x = ()
    
    if a == 0:
        if b == 0:
            flag = -1
            x = ()
        else:
            flag = 1
            x = (-c / b,)
    else:
        delta = b * b - 4 * a * c
        
        if delta < 0:
            flag = 0
            x = ()
        elif delta == 0:
            flag = 1
            x = (-b / (2 * a),)
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            flag = 2
            x = (x1, x2)
    
    return flag, x

# Kết nối bài
a, b, c = NhapDuLieu()
# Gọi hàm giải
flag, x = GiaiPhuongTrinhBac2(1, 5, 6)
# Xuất dữ liệu
s = f'Phuong trinh bac 2 {a}x^2 + {b}x + {c} = 0'
if flag == -1:
    print(f'{s} co vo so nghiem!')
elif flag == 0:
    print(f'{s} vo nghiem!')
elif flag == 1:
    print(f'{s} co 1 nghiem, x = {x[0]}!')
elif flag == 2:
    print(f'{s} co 2 nghiem, x1 = {x[0]}, x2 = {x[1]}!')
# if