#Ví dụ về sử dụng assert
def tinhTb(hk1,hk2):
    assert(hk1>=0 and hk2 >=0),'cả điểm hk1 và hk2 phải >=0!'
    tb=(hk1+hk2*2)/3
    return tb
print(tinhTb(8,7.5))
print(tinhTb(-1,6))
