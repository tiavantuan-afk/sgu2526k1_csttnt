s = input("Moi ban nhap chuoi ky so s: ")

en  = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
vi  = ["khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"]
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
""" CÁC BẠN LÀM BÀI Ở ĐÂY """
#Chuyen thanh chu thuong easy to so sanh
s_low = s.lower()

if s_low in en:
    #Tim vi tri cua tu do
    idx = en.index(s_low)
    #Lay gia tri tuong ung o cac danh sach
    val_num = num[idx]
    val_vi = vi[idx]
    
    print('Chuoi vua nhap hop le')
    print(f'"{s}" bieu dien cho "{val_num}" va ung voi Tieng Viet "{val_vi}"')
else:
    print('Chuoi vua nhap khong hop le!')
# ...