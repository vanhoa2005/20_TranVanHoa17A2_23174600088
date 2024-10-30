# Viết thuật giải nhập từ bàn phím một số tự nhiên N và in ra các số nguyên trong phạm vi từ 1 đến N.
n=int(input("Nhập số tự nhiên n:"))
if n>0:
    print("Các số tự nhiên từ 1 đến n là:")
    for i in range(1,n+1):
        print(i)
else:
    print("n là số tự nhiên")       

