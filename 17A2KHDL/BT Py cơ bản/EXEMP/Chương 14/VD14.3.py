while True: # VÍ dụ về Sytax error
    try:
        x=int(input("Nhập số x="))
        break
    except ValueError:
        print('BỊ lỗi,xin mời nhập lại')
print("x=",x)        
