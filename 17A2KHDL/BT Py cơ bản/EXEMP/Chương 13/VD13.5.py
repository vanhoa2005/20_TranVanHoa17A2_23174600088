#Ví dụ về con trỏ tập tin, hàm tell(), seek()
f= open("bai_tho.txt","r+")
a=f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung là:\n',a)
b = f.tell # Kiểm tra vị trí hiện tại
print('Vị trí hiện tại:,b')
f.seek(0) # Đặt lại ví trí con trỏ tại vị trí đầu file
c=f.read(12)
print('Các ký tự đọc được sau khi về vị trí đầu tiên là:\n',c)
