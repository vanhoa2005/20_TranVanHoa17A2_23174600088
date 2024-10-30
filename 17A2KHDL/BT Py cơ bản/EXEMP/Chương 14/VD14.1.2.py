try:
    value=int(input("Nhập vào một số:"))
    result = 10/ value
except ValueError:
    print("Đó không phải là một giá trị hợp lệ.") 
except:
    print("Một lỗi không xác định đã xảy ra.") 
else:
    print("Không có lỗi xảy ra. Kết quả là :")          