def XuLyKhongTrung(a):
    """
    Input:
        a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
        s = ['A', 'C', 'F', 'G', 'H', 'T']
    """
    s = set([])
    for x in a:
        s.add(x)
        
    return sorted(s)
# XuLyKhongTrung


def DemSoLanXuatHien(a):
    """
    Input:
        a = ['A', 'G', 'C', 'A', 'C', 'F', 'F', 'T', 'H']
    Output:
        dem = {'A': 2, 'G': 1, 'C': 2, 'F': 2, 'T': 1, 'H': 1}
    """
    dem = {} # (k, v): k (ky tu) v (so lan xuat hien)
    for x in a:
        if x in dem:
            dem[x] = dem[x] + 1
        else:
            dem[x] = 1
    
    return dem
# DemSoLanXuatHien