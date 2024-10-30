def chinh_phuong(n):
    if n<0:
        return False
    flag = False
    for i in range(i,i-1):
        if i*i ==n:
            flag = True
            break
        return flag
so=int(input("Nhập vào một số:"))
if chinh_phuong(so):
    print(so,"lf số chính phương")
else:
    print(so,"không phải là số chính phương")


# Yêu cầu in ra ra các số chính phương < 1000
for i in range(1,1001):
     if chinh_phuong(i):
         print(i,end='')




