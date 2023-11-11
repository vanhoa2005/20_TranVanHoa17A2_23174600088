#4.1
a = float(input("Nhập số cần tính bình phương: "))
if a > 0:
    b =a**2
    print(f"Bình phương của {a} là {b}")
else:
    print("Số bạn nhập không phải số dương.")
#4.2
n=int(input("Nhập 1 số nguyên bất kỳ:"))
print("các số nguyên từ 1 đến ",n,"là:")
for i in range(1,n+1):
    print(i)
#4.3
m = int(input("Nhập số tự nhiên m:"))
n = int(input("Nhập số tự nhiên n (n>m):"))
if m>= n:
    print("Vui lòng nhập m<n.")
else:
    print(f"Các số chia hết cho m trong khoảng từ 1 đến {n} là:")
    for i in range(1, n+1):
        if i % m ==0:
            print(i)
#4.4
number1 = float(input("Nhập số thứ nhất:"))
number2 = float(input("Nhập số thứ hai:"))
number3 = float(input("Nhập số thứ ba:"))
max_number = max(number1, number2, number3)
print("Số lớn nhất trong ba số là:", max_number)