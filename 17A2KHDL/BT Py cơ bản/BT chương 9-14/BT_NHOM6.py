def menu():
    while True:
        print("-" * 20)
        print("Chương trình theo dõi sức khỏe")
        print("-" * 20)
        print("1. Nhập thông tin theo dõi")
        print("2. Phân tích dữ liệu sức khỏe")
        print("3. Xem báo cáo")
        print("4. Thoát")
        print("-" * 20)
        choice = input("Chọn chức năng: ")
        if choice not in ["1", "2", "3", "4"]:
            print("Lựa chọn không hợp lệ!")
            continue
        return choice
def nhap_thong_tin():
    ten = input("Nhập tên: ")
    chieu_cao = float(input("Nhập chiều cao (m): "))
    can_nang = float(input("Nhập cân nặng (kg): "))
    muc_hoat_dong = input("Nhập mức hoạt động (nhẹ, trung bình, nặng): ")
    thoi_gian = float(input("Nhập thời gian hoạt động (giờ): "))
    return ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian
def phan_tich_du_lieu(ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian):
    bmi = can_nang / (chieu_cao * chieu_cao)
    calo_tieu_thu = 0
    if muc_hoat_dong == "nhẹ":
        calo_tieu_thu = can_nang * thoi_gian * 2.3
    elif muc_hoat_dong == "trung bình":
        calo_tieu_thu = can_nang * thoi_gian * 3.8
    elif muc_hoat_dong == "nặng":
        calo_tieu_thu = can_nang * thoi_gian * 6.0
    return bmi, calo_tieu_thu
def ghi_du_lieu(ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian, bmi, calo_tieu_thu):
    with open("danh_sach_theo_doi.csv", "a") as f:
        f.write(f"{ten},{chieu_cao},{can_nang},{muc_hoat_dong},{thoi_gian},{bmi},{calo_tieu_thu}\n")
def hien_thi_du_lieu():
    with open("danh_sach_theo_doi.csv", "r") as f:
        data = f.readlines()
    for line in data:
        print(line.strip())
def sap_xep_du_lieu():
    with open("danh_sach_theo_doi.csv", "r") as f:
        data = f.readlines()
    data = sorted(data, key=lambda line: float(line.split(",")[5])) # Sắp xếp theo BMI
    for line in data:
        print(line.strip())
while True:
    choice = menu()
    if choice == "1":
        ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian = nhap_thong_tin()
        bmi, calo_tieu_thu = phan_tich_du_lieu(ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian)
        ghi_du_lieu(ten, chieu_cao, can_nang, muc_hoat_dong, thoi_gian, bmi, calo_tieu_thu)
        print("Đã lưu thông tin.")
    elif choice == "2":
        hien_thi_du_lieu()
    elif choice == "3":
        sap_xep_du_lieu()
    elif choice == "4":
        break