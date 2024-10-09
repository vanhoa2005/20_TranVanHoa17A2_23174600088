from datetime import date

class Employee:
    def __init__(self, ho_ten, ngay_sinh, ngay_vao_cong_ty):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.ngay_vao_cong_ty = ngay_vao_cong_ty

    def __str__(self):
        return f"Tên: {self.ho_ten}\nNgày sinh: {self.ngay_sinh}\nNgày vào công ty: {self.ngay_vao_cong_ty}"

# Danh sách nhân viên (ban đầu chưa có nhân viên nào)
nhan_vien = []

# Hàm để thêm một nhân viên mới vào danh sách
def them_nhan_vien():
    ho_ten = input("Nhập họ tên: ")
    ngay_sinh = date(int(input("Nhập năm sinh: ")), int(input("Nhập tháng sinh: ")), int(input("Nhập ngày sinh: ")))
    ngay_vao_cong_ty = date(int(input("Nhập năm vào công ty: ")), int(input("Nhập tháng vào công ty: ")), int(input("Nhập ngày vào công ty: ")))
    nhan_vien.append(Employee(ho_ten, ngay_sinh, ngay_vao_cong_ty))
    print("Đã thêm nhân viên thành công!")

# Hàm để hiển thị thông tin tất cả nhân viên
def hien_thi_nhan_vien():
    if len(nhan_vien) == 0:
        print("Danh sách nhân viên đang trống.")
    else:
        for nv in nhan_vien:
            print(nv)

# Menu chính
while True:
    print("\n--- Quản lý nhân viên ---")
    print("1. Thêm nhân viên")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Thoát")
    chon = int(input("Chọn chức năng: "))

    if chon == 1:
        them_nhan_vien()
    elif chon == 2:
        hien_thi_nhan_vien()
    elif chon == 3:
        break
    else:
        print("Lựa chọn không hợp lệ!")