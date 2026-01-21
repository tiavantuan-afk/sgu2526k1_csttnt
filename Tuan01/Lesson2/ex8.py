
def NhapMang():
    """
    Input:
        Ban phim = 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2
    Output:
        a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    """
    input_str = input('Moi ban nhap mang (cach nhau khoang trang): ').split()
    a = []
    for x in input_str:
        a.append(int(x))
    return a



def XuatMang(a):
    """
    Input:
        a = [1, 4, 1, 2, 3, 4, 1, 2, 3, 3, 1, 2, 3, 4, 10, 2]
    Output: 
        In ra man hinh:
            Mang co 16 phan tu: 1 4 1 2 3 4 1 2 3 3 1 2 3 4 10 2 
    """
    print(f'Mang co {len(a)} phan tu:', end=' ')
    for x in a:
        print(x, end = ' ')
    
# XuatMang



import random
def SinhNgauNhien(n, vmin = -10, vmax = 10):
    """
    Input:
        n = 30, vmin = -10, vmax = 10
    Output:
        a = [-1, -4, -8, 6, 4, -5, -1, -4, -9, -5, -10, 0, -6, 2, 1, -9, -9, 10, -8, -9, -7, 9, 2, -4, -1, -6, 5, -6, 9, -8]
    """    
    a = []
    for i in range(n):
        giatri = random.randint(vmin, vmax)
        a.append(giatri)
    return a
# SinhNgauNhien



def DemTongChanLe(a):
    """
    Input: a[] = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -2, -10, -8, -3, 2, -7, -10, 6, 0]
    Output: tong, sochan, sole
    """
    tong = 0
    sochan = 0
    sole = 0
    
    for x in a:
        tong = tong + x
        if x%2==0:
            sochan = sochan + 1
        else:
            sole = sole + 1
    
    return tong, sochan, sole
# DemTongChanLe



def DayChanLe(a): # Gia tri tra ve
    """
    Input:
        a = [1, 4, 2, 0, -1, -7, 3, -6, 4, 9, -5, 7, 7, -7, -10, 1, -10, 9, -4, -6, 10, -2, -10, -8, -3, 2, -7, -10, 6, 0]
    Output: (achan, ale)
        achan = [4, 2, 0, -6, 4, -10, -10, -4, -6, 10, -2, -10, -8, 2, -10, 6, 0]
        ale = [1, -1, -7, 3, 9, -5, 7, 7, -7, 1, 9, -3, -7]
    """    
    achan = []
    ale = []
    
    for x in a:
        if x%2==0:
            achan.append(x)
        else:
            ale.append(x)
    return achan, ale
# DayChanLe

