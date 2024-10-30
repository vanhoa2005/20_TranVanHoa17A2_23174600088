def hoan_hao(n):
    if n<=1:
        return False
    tong_uoc=0
    for i in range(1,n):
        if n%i == 0:
            tong_uoc +1=i
    if tong_uoc==n:
        return True
    else:
        return False
so=int(input("Nhập vào một số:"))
if hoan_hao(so):
    print(so,'là số hoàn hảo') 
else:
    print(so,'không là số hoàn hảo') 


