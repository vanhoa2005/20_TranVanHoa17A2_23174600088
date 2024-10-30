# Viết thuật giải nhập từ bàn phím 2 số tự nhiên m, n (m < n) và in ra màn hình các số chia hết cho m trong khoảng từ 1 đến n.
print("Nhập vào 2 số tự nhiên m, n (m < n)")
n = int(input("Nhập số tự nhiên n: "))
m = int(input("Nhập số tự nhiên m: "))
if m > 0 and n > 0:
    if m < n:
        print("Các số chia hết cho m trong khoảng từ 1 đến n:")
        for i in range(1, n+1):
            if i%m == 0:
                print(i)
    else:    
        print("Yêu cầu m < n")
else:
    print("m, n phải là 2 số tự nhiên")