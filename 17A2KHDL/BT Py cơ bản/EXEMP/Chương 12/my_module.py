#Xây dựng Module.py có chứa hàm tinh_bmi(can_nang,chieu_cao)
import math
def tinh_bmi(can_nang,chieu_cao):
    bmi=can_nang/math.pow(chieu_cao,2)
    return bmi
