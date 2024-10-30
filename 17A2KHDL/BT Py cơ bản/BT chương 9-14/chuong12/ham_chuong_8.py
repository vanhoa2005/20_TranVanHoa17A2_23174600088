import math
# 8.1
def max_min_numbers(a,b,c,d):
    a_max = a
    if b > a_max:
        a_max = b
    if c > a_max:
        a_max = c
    if d > a_max:
        a_max = d
    a_min = a
    if b < a_min:
        a_min = b
    if c < a_min:
        a_min = c
    if d < a_min:
        a_min = d
    print("Giá trị lớn nhất:", a_max)
    print("Giá trị nhỏ nhất:", a_min)
#8.2
def abs(x):
    print(abs(x))

#8.3
def giai_pt_bac_nhat(a, b):
    
    if a != 0 and b != 0:
        print("phương trình có nghiệm là",-b/a)
    elif a == 0 and b == 0 :
        print("phương trình vô số nghiệm")
    else: 
        print("phương trình vô nghiệm")
#8.4
def kiemtratamgiac(a,b,c):
    
    if a+b <c and b+c<b:
        print("day khong phai la tam giac")
    else:
        print("day la mot tam giac")
    p=(a+b+c)/2
    S= (p*(p-a)*(p-b)*(p-c))**0.5
    print("Dien tich tam giac tren la: ",S)
#8.5 
def namnhuan(x):   
    
    if (x % 4 == 0 and x % 100 != 0) or (x% 400 == 0):
        print("Năm đó là năm nhuận.")
    print("Năm đó không phải là năm nhuận.")

#8.6
def cuoc_xe_taxi(loai_xe,so_km,thoi_gian_cho,tien_cho):

    if thoi_gian_cho >=5:
        tien_cho = (thoi_gian_cho-5)*0.8
    if loai_xe==4:
        if so_km <=0.8:
            tien_di_chuyen=0.8*11000
        elif so_km <=20:
            tien_di_chuyen=0.8*11000+(20-so_km)*12100
        else:
            tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
            tien_cuoc=tien_cho+tien_di_chuyen
            print("Cước phí xe taxi 4 chỗ của quý khách là ",tien_cuoc)
    else:
        if so_km <=0.8:
            tien_cuoc+tien_cho+0.8*13000
        elif so_km <=30:
            tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
        else:
            tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
            tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 7 chỗ của quý khách là" ,tien_cuoc)


#8.7
def tinh_tien_dien(kwh):
    kwh = float(input("Nhập số Kwh tiêu thụ: "))
    bang_gia = {
    "Bậc 1": {"kwh": 0, "đơn giá": 1678},
    "Bậc 2": {"kwh": 51, "đơn giá": 1734},
    "Bậc 3": {"kwh": 101, "đơn giá": 2014},
    "Bậc 4": {"kwh": 201, "đơn giá": 2536},
    "Bậc 5": {"kwh": 301, "đơn giá": 2834},
    "Bậc 6": {"kwh": 401, "đơn giá": 2927}
    }
    def hoa_don_dien(kwh):
        tong_gia = 0
        for i in range(bang_gia):
            if kwh <=bang_gia[i]["kwh"]:
                tong_gia += kwh * bang_gia[i]["đơn giá"]
                break
            else:
                kwh -= bang_gia[i]["kwh"]
                tong_gia += bang_gia[i]["kwh"] * bang_gia[i]["đơn giá"]
            return tong_gia
    tong_gia = hoa_don_dien(kwh)
    print("Tổng tiền điện phải trả là:", tong_gia)

#8.8
def thuephong():
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
def Countdown(thoi_gian):
    
    while thoi_gian > 0:
        print(thoi_gian)
        thoi_gian -= 1
    print("Start!!!")

#8.10
def bieuthuc(n,x):
    
    S=(x**2+1)**n
    print("S=",S)

#8.11
def bieuthuc11(n,x):
    n= eval(input("Nhập n: "))
    x= eval(input("Nhập x: "))
    S=(x**2+x+1)**n+(x**2-x+1)**n
    print("S=",S)
#8.12
def so_nguyen_to(n):
    
    if n <= 1:
        so_nguyen_to = False
    else:
        so_nguyen_to = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                prime = False
                break
    if so_nguyen_to(n):
        print(f"{n} là số nguyên tố")
    else:
        print(f"{n} không phải là số nguyên tố")

#8.13
def tinhbieuthuc(n):
    
    A = sum(i for i in range(n + 1) if i % 2 != 0)
    print("A =", A)
    B = sum(i for i in range(n + 1) if i % 2 == 0)
    print("B =", B)
    C = 1
    for i in range(1, n + 1):
        C *= i
    print("C =", C)
    D = 1
    for i in range(1, n + 1):
        if i % 3 == 0:
            D *= i
    print("D =", D)
    def is_prime(number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
    E = sum(i for i in range(2, n + 1) if is_prime(i))
    print("E =", E)
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= 1 / i
        else: 
            total += 1 / i
    print("F =", total)

#8.14
def tong14(n):
    tong = 0
    
    for i in range(n):
        so_nguyen = int(input(f"Nhập số nguyên thứ {i+1}: "))
        tong += so_nguyen
    print(f"Tổng của các số nguyên là: {tong}")
#8.15
def tong15():
    tong = 0
    while True:
        so_nguyen = int(input("Nhập một số nguyên (Nhập 0 để kết thúc): "))
        if so_nguyen == 0:
            break  # Thoát khỏi vòng lặp nếu nhập số 0
        else:
            tong += so_nguyen
    print(f"Tổng của các số nguyên là: {tong}")
#8.16
def ucln(a,b):
    a = int(input("Nhập số nguyên a: "))
    b = int(input("Nhập số nguyên b: "))
    while b :
        a, b = b, a % b
        print("ước chung nhỏ nhất  của 2 số là ",a)
#8.17
def bcnn(a, b):

    if a <= 0 or b <= 0:
        raise ValueError("a và b phải là số nguyên dương")

    bcnn = 1
    for i in range(2, int(max(a, b) ** 0.5) + 1):
        if a % i == 0 and b % i == 0:
            bcnn *= i
    result =  bcnn * max(a // bcnn, b // bcnn)
    print(f"Bội chung lớn nhất của ({a}, {b}) là: {result}")
#8.18
def sohoanhao(n):
  tong = 0
  i = 1
  while (tong < n):
    if (n % i == 0):
      tong += i
    i += 1
  if (tong == n):
    print(n, " là số hoàn hảo")
  else:
    print(n, " không phải là số hoàn hảo")
#8.19
def daonguocso(numbers):
    number_list = numbers.split() 
    number_list = [int(num) for num in number_list]
    odd_numbers = [num for num in number_list if num % 2 != 0][::-1]
    for odd_num in odd_numbers:
        print(odd_num, end=" ")
#8.20
def solve_equation(n,x):
    
    while True:
        calculated = 1 + (x**2) / n
        real_value = math.exp(x)
        if abs(calculated - real_value) < 1e-4:
            break  
        x += 0.1  
    print(f"Giá trị của công thức với độ chính xác 10^-4: {calculated}")