#8.1
x=int(input("Nhập vào giá trị của x :"))
if x<0:
    print("Giá trị tuyệt đối của x là :",-1*x)
else :
    print("Giá trị tuyệt đối của x là :",x)
#8.2
a,b,c,d=map(int,input("Nhập vào 4 số tư nhiên bất kỳ :"))
print("Số lớn nhất trong 4 chữ số là :",max(a,b,c,d))
print("Số nhỏ nhất trong 4 chữ số là :",min (a,b,c,d))
#8.3
print("Phương trình bậc nhất dạng : ax+b=0")
a=int(input("Nhập vào giá trị của a :"))
b=int(input("Nhập vào giá trị của b :"))
if a != 0:
    print("Với a khác 0 pt có nghiệm x=-b/a")
    x=-b/a
    print("Nghiệm của phương trình là :",x)
else:
    print("Phương trình vô nghiệm ")
#8.4
import math
a=float(input("Nhập vào độ dài cạnh a:"))
b=float(input("Nhập vào độ dài cạnh b"))
c=float(input("Nhập vào độ dài cạnh c"))
p=(a+b+c/2)
print("Diện tích tam giác là:",math.sqrt(p*(p-a)*(p-b)*(p-c)))
#8.5
nam=int(input("Nhập năm:"))
if((nam%4==0)and(nam%100!=0))or (nam%400==0):
    print("Năm đó là năm nhuận")
else:
    print("Năm đó là năm không nhuận ")
#8.6
loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
so_km=float(input("Nhập số km chạy bằng = "))
time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cuoc=float(0)
tien_di_chuyen=float(0)
if time_cho >=5:
    tien_cho=(time_cho-5)*0.8
else:
    tien_cho=0
if loai_xe==4:
    if so_km <=0.8:
        tien_di_chuyen=0.8*11000
    elif so_km <=20:
        tien_di_chuyen=0.8*11000+(20-so_km)*12100
    else:
        tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
if loai_xe==7:
    if so_km <=0.8:
        tien_cuoc+tien_cho+0.8*13000
    elif so_km <=30:
        tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
    else:
        tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)
#8.7
print("Tiền điện dân dụng ")
a=int(input("Mời nhập vào số điện :"))
if ((a>0)and(a<=50)) :
    tien_dien_bac1=a*1.678
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac1)
elif ((a>50)and(a<=100)):
    tien_dien_bac2=a*1.734 
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac2)  
elif ((a>100)and(a<=200)):
    tien_dien_bac3=a*2.014
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac3)
elif ((a>200)and(a<=300)):
    tien_dien_bac4=a*2.536
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac4)
elif ((a>300)and(a<400)):
    tien_dien_bac5=a*2.834
    print("Số tiền điện phải trả của gia đình là",tien_dien_bac5)
elif ((a>400)):
    tien_dien_bac6=a*2.927
    print("Số tiền điện phải trả của gia đình là :",tien_dien_bac6)
#8.8
print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
if a>0&a<=8:
    if a==1: c=1260000
    elif a==2: c=1550000
    elif a==3: c=1830000
    elif a==4: c=1830000
    elif a==5: c=2120000
    elif a==6: c=2120000
    elif a==7: c=2540000
    elif a==8: c=4800000
    else: 
        print("Vui lòng chọn lại mã loại phòng.")
else: print("Vui lòng chọn lại mã loại phòng.") 
if b==1:
    print("Giá  tiền phải trả là:",c,"đồng.")
elif b==2:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b==3:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b>=4:
    print("Giá  tiền phải trả là:",c*b*0.7,"đồng.")       
else:
    print("Vui lòng nhập lại số đêm.")
#8.9
a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)
#8.10
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)
#8.11
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
A=(x*x+x+1)**n + (x*x-x+1)**n
print("A=(x*x+x+1)^n+(x*x-x+1)^n=",A)
#8.12
n = int(input("Nhập số n = "))
flag = True 
if n < 2 :
    print(n, "Không nguyên tố !!!")
else:
    for i in range(2, n):
        if n%i == 0:
            flag = False
            break
    if flag:
        print(n, " là số nguyên tố")
    else:
        print(n, " không phải là số nguyên tố!!!")
#8.14
# Khởi tạo biến tổng
tong = 0

# Số lượng số nguyên cần tính tổng
n = int(input("Nhập số lượng số nguyên: "))

# Nhập các số nguyên và tính tổng
for i in range(n):
    so_nguyen = int(input(f"Nhập số nguyên thứ {i+1}: "))
    tong += so_nguyen

# In kết quả tổng
print(f"Tổng của các số nguyên là: {tong}")
#8.15
# Khởi tạo biến tổng
tong = 0

while True:
    so_nguyen = int(input("Nhập một số nguyên (Nhập 0 để kết thúc): "))
    
    if so_nguyen == 0:
        break  # Thoát khỏi vòng lặp nếu nhập số 0
    else:
        tong += so_nguyen

print(f"Tổng của các số nguyên là: {tong}")
#8.16
# Hàm tính UCLN
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tìm và in ra UCLN của a và b
ucln_ab = ucln(a, b)
print(f"Ước chung lớn nhất của {a} và {b} là: {ucln_ab}")
#8.17
# Hàm tính BCNN
def bcnn(a, b):
    return (a * b) // ucln(a, b)

# Hàm tính UCLN
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính và in ra BCNN của a và b
bcnn_ab = bcnn(a, b)
print(f"Bội chung lớn nhất của {a} và {b} là: {bcnn_ab}")
#8.18
print("Nhập vào số N lớn hơn 0: ")
n = int(input())
tong = 0
for i in range(1, n):
    if (n % i == 0):
        tong += i
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")