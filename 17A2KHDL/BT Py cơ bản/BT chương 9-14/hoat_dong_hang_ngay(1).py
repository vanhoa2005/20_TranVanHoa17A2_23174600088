print("Nhập giá trị (1) nếu bạn hoạt động nhẹ")
print("Nhập giá trị (2) nếu bạn hoạt động trung bình")
print("Nhập giá trị (3) nếu bạn hoạt động mạnh")
def calo(a,b,c):
    calo=a*b*c*2.3
    input("Mức hoạt động bình thường!")
can_nang=float(input("Hãy nhập cân nặng của bạn (kg):"))   
chieu_cao=float(input("Hãy nhập cân nặng của bạn (m):")) 
thoi_gian=float(input("Hãy nhập thời gian vận động (giờ);"))
calo(chieu_cao,can_nang,thoi_gian)
