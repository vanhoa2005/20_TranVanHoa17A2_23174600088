a=int(input("Nhập một số nguyên dương nhỏ hơn 100:"))
if a<=0:
    raise ValueError("Bạn đã nhập một số quá nhỏ:))")
if a>=100:
    raise ValueError("Bạn cần nhập một số nhỏ hơn 100!")
except ValueError as ex:
print(ex)