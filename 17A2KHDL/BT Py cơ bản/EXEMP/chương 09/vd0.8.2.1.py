#viết hàm tính giai thừa theo thuật giải đệ qui
def giaithua(n):
    if n==1:
        return 1
    else:
        return(n* giaithua(n-1))
    number1 = 5
    number2 =int(input("Nhập số cần tính giai thừa :" ))
    print("Giai thừa của",number1,"là",giaithua(number1))
    print("Giai thừa của",number2,"là",giaithua(number2))
    
     
          