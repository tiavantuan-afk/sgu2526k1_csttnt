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

# Kiểm tra
a, b, c = NhapDuLieu()
