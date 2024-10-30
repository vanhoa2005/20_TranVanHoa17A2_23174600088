from ham_chuong_8 import max_min_numbers,giai_pt_bac_nhat,abs,kiemtratamgiac,namnhuan,cuoc_xe_taxi,tinh_tien_dien,thuephong,Countdown,bieuthuc,solve_equation,daonguocso,tinhbieuthuc,sohoanhao,so_nguyen_to,tong15,tong14,ucln,bcnn
#8.1
a, b, c, d = int(input("Nhập a: ")), int(input("Nhập b: ")), int(input("Nhập c: ")), int(input("Nhập d: "))
max_min_numbers(a,b,c,d)
#8.2
x=int(input("Nhập x: "))
abs(x)
#8.3
a, b = float(input("Nhập a: ")), float(input("Nhập b: "))
giai_pt_bac_nhat(a, b)
#8.4
a = float(input("nhap do dai canh a: "))
b = float(input("nhap do dai canh b: "))
c = float(input("nhap do dai canh c: "))
kiemtratamgiac(a,b,c)
#8.5
x=int(input("Nhập năm: "))
namnhuan()
#8.6
loai_xe=int(input("Cho biết loại xe là 4 hay 7 ?"))
so_km=float(input("Nhập số km chạy bằng = "))
thoi_gian_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cho = 0
cuoc_xe_taxi(loai_xe,so_km,thoi_gian_cho,tien_cho)
#8.7
kwh = float(input("Nhập số Kwh tiêu thụ: "))
tinh_tien_dien(kwh)
#8.8
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
thuephong(a,b)
#8.9
thoi_gian = int(input("Nhập thời gian  (giây): "))
Countdown(thoi_gian)
#8.10
n= eval(input("Nhập n: "))
x= eval(input("Nhập x: "))
bieuthuc(n,x)
#8.11
n = int(input("Nhập một số nguyên dương: "))
so_nguyen_to(n)
#8.12
n = int(input("Nhập số lượng số nguyên: "))
#8.13
n=int(input("Nhập một số nguyên : "))
tinhbieuthuc(n)
#8.14
n = int(input("Nhập số lượng số nguyên: "))
tong14(n)
#8.15
tong15()
#8.16
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
ucln(a,b)
#8.17
a, b, = int(input("Nhập a: ")), int(input("Nhập b: "))
bcnn(a, b)
#8.18
n = int(input("nhập số nguyên dương:"))
sohoanhao(n)
#8.19
numbers = int("nhập các số cách nhau bởi mỗi dấu cách")
daonguocso(numbers)
#8.20
n = int(input("nhập x:"))
x = int(input("nhập x:"))
solve_equation(n,x)


