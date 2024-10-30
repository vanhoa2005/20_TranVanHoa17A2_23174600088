# CHƯƠNG 9


# câu 1
def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0
n = float(input("Nhập số:"))
print(sign(n))

# câu 2
def can(year):
    can_list = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    c = (year + 6) % 10
    return can_list[c]
def chi(year):
    chi_list = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    i = (year + 8)% 12
    return chi_list[i]

def get_lunar_year(year):
    return can(year) + " " + chi(year)
year = int(input("Nhập năm dương lịch: "))
print("Năm", year, "lịch âm là năm", get_lunar_year(year))

# câu 3
def BMI(c,b):
    bmi = c / (b ** 2)
    bmi = round(bmi, 2)
    print("Chỉ số BMI của bạn là:", bmi)
    if bmi < 18.5:
        print("Bạn nhẹ cân.")
    elif 18.5 <= bmi < 25:
        print("Bạn bình thường.")
    else:
        print("Bạn béo phì.")
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
BMI(can_nang,chieu_cao)

#câu 4
def tinh_S(n, x):
    return (x**2 + 1)**n 
n = float(input("Nhập n:"))
x = float(input("Nhập x :"))
print("S =", tinh_S(x, n))

# câu 5
def tinh_A(n, x):
    return (x**2 + x + 1)**n + ( x**2 - x + 1)**n
n = float(input("Nhập n:"))
x = float(input("Nhập x:"))
print("A =", tinh_A(x, n))

# câu 6
def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    flag = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            flag = True
            break
    if flag:
        return False
    else:
        return True
n = int(input("Nhập số:"))
print(kiem_tra_so_nguyen_to(n))
  
#câu 7
def phan_nguyen(a, b):
    return a // b
a = int(input("Nhập a :"))
b = int(input("Nhập b :"))
print("Phần nguyên là:",phan_nguyen(a, b))

#câu 8
def kiem_tra_so_hoan_hao(n):
    flag=True
    if n<0:
        return flag
    else:
        sum=0
        for i in range(1,n):
            if n%i==0:
                sum+=1
            if sum==n:
                flag=True
                return flag


n = int(input("Nhập n :"))
if(kiem_tra_so_hoan_hao(n)):
    print(n,"là số hoàn hảo")
else:
    print(n,"không là số hoàn hảo")


#câu 9
r,a,b = float(input("Nhập r:")),float(input("Nhập a:")),float(input("Nhập b:"))
dien_tich_tron = lambda r: 3.14 * r**2
chu_vi_tron = lambda r: 2 * 3.14 * r
dien_tich_hcn = lambda a, b: a * b
chu_vi_hcn = lambda a, b: 2 * (a + b)
print("Diện tích hình tròn:", dien_tich_tron(r))
print("Chu vi hình tròn:", chu_vi_tron(r))
print("Diện tích hình chữ nhật:", dien_tich_hcn(a, b))
print("Chu vi hình chữ nhật:", chu_vi_hcn(a, b))








#CHUONG 10



#10.1
print(max(3,6,8))
print(min(4,248,6))
#10.2
print(abs(-7))
#10.3
x = int(input())
n = int(input())
print(pow((pow(x,2)+1,n)))
#10.4
x = int(input())
n = int(input())
print(pow((pow(x,2)+x+1),n)+pow((pow(x,2)-x+1),n))
#10.5
def zipcode(n):
     return len(str(n)) == 6
n = int(input())     
print(zipcode(n))
#10.6
a,b,c = int(input()),int(input()),int(input())
denta = b**2 - 4*a*c
if a == 0 or denta < 0 : print("vô nghiệm")
elif denta == 0 : print("phương trình có nghiệm kép là",-b/a)
else : print(" phương trình có 2 nghiệm x1,x2 lần lượt là",(-b + denta)/a,(-b - denta)/a)
#10.8
from datetime import datetime

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

ngay_thang_nam = datetime(nam, thang, ngay).date()

print("Ngày tháng năm vừa nhập:", ngay_thang_nam.strftime("%d - %m - %Y"))

if ngay_thang_nam.year % 4 == 0 and (ngay_thang_nam.year % 100 != 0 or ngay_thang_nam.year % 400 == 0):
    print("Năm", ngay_thang_nam.year, "là năm nhuận")
else:
    print("Năm", ngay_thang_nam.year, "không là năm nhuận")

thu_trong_tuan = ngay_thang_nam.strftime("%A")
thu_trong_tuan_vn = {"Monday": "Thứ Hai", "Tuesday": "Thứ Ba", "Wednesday": "Thứ Tư", "Thursday": "Thứ Năm", "Friday": "Thứ Sáu", "Saturday": "Thứ Bảy", "Sunday": "Chủ Nhật"}

print(ngay_thang_nam.strftime("%d - %m - %Y"), "là", thu_trong_tuan_vn[thu_trong_tuan])

so_ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ngay_thang_nam.year % 4 == 0 and (ngay_thang_nam.year % 100 != 0 or ngay_thang_nam.year % 400 == 0):
    so_ngay_trong_thang[1] = 29
print("Số ngày trong tháng", ngay_thang_nam.month, "là:", so_ngay_trong_thang[ngay_thang_nam.month - 1])\






# CHƯƠNG 11
# BT 11.1
""" 
độ dài danh sách a là 3
độ dài danh sách b là 2
độ dài danh sách c là 0
độ dài danh sách d là 2
"""


# BT 11.2
teams = [['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'], ['David', 'Jack', 'Bill', 'Tom', 'Mike'], ['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
print(teams[2][1])



# BT 11.3
List_of_animals =  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo'] 
n = input(" I want to find")
print("List of animals :  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']")
print("Number of animals",len(List_of_animals))
if n in List_of_animals:
    print("There is ",n,"list of animals")
else:
    print("There isn't ",n,"list of animals")



# BT 11.5
list=[]
x=int(input("Nhập giá trị:"))
list.append(x)
i=1
while i==1:
          y=int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không"))
          if y==1:
                  x=int(input("Nhập giá trị:"))
                  list.append(x)
          elif y==0:
                  break
print("list:",list)
sum=0
for num in list:
        sum+=num
print("Tổng các giá trị trong list:",sum)
x=int(input("Nhập giá trị cần tìm:"))
find = x in list
if find=="True":
        print(x,"xuất hiện",list.count(x),"lần trong list")
for i in list:
        if i>x:
          print(x,"không lớn hơn tất cả các số trong list")
          break
new_list=[]
for i in list:
        if i>x:
               new_list.append(i)
print("Các số lớn hơn",x,"trong list:",new_list)   




# BT 11.4
list = []
while True:
  value = int(input("Nhập giá trị: "))
  list.append(value)
  choice = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
  if choice == 0:
    break
print("List: ", list)
total = sum(list)
print("Tổng các giá trị trong list: ", total)
x = int(input("Nhập vào giá trị cần tìm x: "))
if x in list:
  count = list.count(x)
  print("{} xuất hiện {} lần trong list".format(x, count))
else:
  print("{} không xuất hiện trong list".format(x))
if x > max(list):
  print("{} lớn hơn tất cả các số trong list".format(x))
else:
  print("{} không lớn hơn tất cả các số trong list".format(x))
  greater_list = [num for num in list if num > x]
  print("Các số lớn hơn {} trong list: {}".format(x, greater_list))


# BT 11.8   
def has_lucky_number(nums):
  for num in nums:
    if num % 7 == 0:
      return True
  return False
nums = [2, 6, 7, 9]
print(has_lucky_number(nums))
#11.6
# Danh sách chiều cao ban đầu (đơn vị: inch)
chieu_cao_inch = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]

# Chuyển đổi từ inch sang mét
chieu_cao_met = [round(chieu * 0.0254,2) for chieu in chieu_cao_inch]

print("Chiều cao ban đầu (m):", chieu_cao_met[:3])
print("3 Chiều cao cuối cùng (m):", chieu_cao_met[-3:])

# Tính chiều cao trung bình
chieu_cao_trung_binh = round(sum(chieu_cao_met) / len(chieu_cao_met),2)
print("Chiều cao trung bình (m):", chieu_cao_trung_binh)

# Tìm chiều cao lớn nhất và nhỏ nhất
print("Chiều cao lớn nhất (m):", max(chieu_cao_met))
print("Chiều cao nhỏ nhất (m):", min(chieu_cao_met))

# Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
print("Danh sách sắp xếp tăng dần:", sorted(chieu_cao_met))
print("Danh sách sắp xếp giảm dần:", sorted(chieu_cao_met, reverse=True))
#11.7
def elementwise_greater_than(L, thresh):
    return [item > thresh for item in L]

# Test with given input
L = [1, 2, 3, 4,5]
thresh = 2
print(elementwise_greater_than(L, thresh))  # This will print [False, False, True, True]
#11.9
def party_late(arrivals, name):
    # Tìm vị trí của tên trong danh sách
    index = arrivals.index(name)
    # Tính số khách của bữa tiệc
    total = len(arrivals)
    # Tính số khách cần đến trước để không bị trễ
    limit = total // 2
    # Kiểm tra xem vị trí của tên có lớn hơn giới hạn và không phải là cuối cùng hay không
    return index > limit and index < total - 1
#11.10
def menu_is_boring(meals):
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

# Thay thế danh sách dưới đây bằng danh sách các bữa ăn thực tế của bạn
meals = ['bữa ăn 1', 'bữa ăn 2', 'bữa ăn 3']  

if menu_is_boring(meals):
    print("Menu này nhàm chán.")
else:
    print("Menu này không nhàm chán.")


# Test with given input
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
print(party_late(arrivals, 'Mona'))  # This will print True
print(party_late(arrivals, 'Owen'))  # This will print False
print(party_late(arrivals, 'Ford'))  # This will print False
#11.11
# Tạo một tuple chứa 10 chuỗi
colors = ('red', 'green', 'yellow', 'blue', 'black', 'white', 'pink', 'orange', 'red', 'blue')

# Nhập index dương và index âm từ người dùng
positive_index = int(input("Nhập index dương (0-9): "))
negative_index = int(input("Nhập index âm (-1 đến -10): "))

# Nhập chuỗi cần tìm
s_find = input("Nhập chuỗi cần tìm: ")

# In giá trị của phần tử trong tuple theo index đã nhập
print(f"Giá trị tại index {positive_index} là {colors[positive_index]}")
print(f"Giá trị tại index {negative_index} là {colors[negative_index]}")

# Đếm số lần xuất hiện của s_find trong tuple và in ra màn hình
count = colors.count(s_find)
print(f"Chuỗi '{s_find}' xuất hiện {count} lần trong tuple")
#11.12
# Tạo tuple a chứa 4 số nguyên dương đầu tiên
a = (1, 2, 3, 4)

# Tạo tuple b chứa 4 số nguyên dương tiếp theo
b = (5, 6, 7, 8)

# Tạo tuple c là sự kết hợp của các phần tử trong tuple a và b
c = a + b

# Tạo tuple d từ tuple c với các phần tử được sắp xếp
d = sorted(c)

# In phần tử thứ ba của d
print("Phần tử thứ ba của d:", d[2])

# In ba phần tử cuối cùng của d
print("Ba phần tử cuối cùng của d:", d[-3:])
#chương 12
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










# CHƯƠNG 14


# câu 1
try:
    a = int(input("Nhập độ dài cạnh a: "))
    b = int(input("Nhập độ dài cạnh b: "))
    c = int(input("Nhập độ dài cạnh c: "))
    if  (a <= 0 and b <= 0 and c <= 0):
        raise ValueError("Các cạnh tam giác phải là số dương")
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Không phải là tam giác")
    print("Các cạnh của tam giác là: a = ", a, ", b = ", b, ", c = ", c)
except ValueError as ex:
    print(ex)


#câu 2
lst=[]
while True:
    n = input("Nhập số nguyên dương: ")
    try:
        n = int(n)
    except ValueError:
        print("Lỗi nhập số ")
        continue
    if n < 0:
        raise ValueError("Lỗi số âm ")
    if n == 0:
        break
    if len(lst) >= 4 and n == lst[-3]:
        raise ValueError("Lỗi nhập lặp lại ")
    if len(lst) >= 5 and n % 2 == 0:
        raise ValueError("Lỗi nhập số chẵn")
    lst.append(n)
print("Danh sách các số :", lst)