m=int(input("Nhập số hàng của ma trận m:"))
n=int(input("Nhập số cột của ma trận n:"))
a=[]
for i in range(m):
    print("Nhập các phần tử của hàng thứ",i+1,":")
    b=[]
    for j in range(n):
        x=input()
        b=b+[x]
        a.append(b)
        print("Ma trận đã nhập vào là")
        for i in range(m):
            for j in range(n):
                print(a[i][j],end="")
                print() 
                
