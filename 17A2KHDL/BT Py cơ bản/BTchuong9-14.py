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