try:
    x=eval(input("Nhập x\n"))
    y=eval(input("Nhập y\n"))
    z=x/y
except NameError as er1:
    print("Error",er1) 
except ZeroDivisionError as er2:
    print("Error",er2)
else:
    print('x/y=',z)           
