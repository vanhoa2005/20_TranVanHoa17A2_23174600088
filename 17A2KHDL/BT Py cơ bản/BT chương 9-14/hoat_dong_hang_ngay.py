def nhap_thong_tin_nguoi_dung():
    """
    Nhập và lưu trữ thông tin cơ bản của người dùng
    """
    ten = input("Nhập tên: ")
    tuoi = int(input("Nhập tuổi: "))
    can_nang = float(input("Nhập cân nặng (kg): "))
    chieu_cao = float(input("Nhập chiều cao (m): "))
    return ten, tuoi, can_nang, chieu_cao

def tinh_bmi(can_nang, chieu_cao):
    """
    Tính chỉ số BMI dựa trên cân nặng và chiều cao
    """
    bmi = can_nang / (chieu_cao * chieu_cao)
    return bmi

def nhap_hoat_dong_hang_ngay():
    """
    Cho phép người dùng nhập thông tin về hoạt động hàng ngày và thời gian thực hiện
    """
    hoat_dong = []
    while True:
        ten_hoat_dong = input("Nhập tên hoạt động (hoặc 'q' để thoát): ")
        if ten_hoat_dong == "q":
            break
        thoi_gian = float(input("Nhập thời gian thực hiện (giờ): "))
        hoat_dong.append((ten_hoat_dong, thoi_gian))
    return hoat_dong

def tinh_calo_tieu_thu(can_nang, hoat_dong):
    """
    Tính lượng calo tiêu thụ dựa trên hoạt động hàng ngày và thông tin cá nhân của người dùng
    """
    calo_tieu_thu = 0
    for ten_hoat_dong, thoi_gian in hoat_dong:
        if ten_hoat_dong == "Đi bộ nhẹ":
            calo_tieu_thu += can_nang * thoi_gian * 2.3
        elif ten_hoat_dong == "Đi bộ nhanh":
            calo_tieu_thu += can_nang * thoi_gian * 3.8
        elif ten_hoat_dong == "Chạy bộ":
            calo_tieu_thu += can_nang * thoi_gian * 6.0
    return calo_tieu_thu

def xuat_bao_cao_suc_khoe(ten, tuoi, bmi, calo_tieu_thu, hoat_dong):
    """
    Hiển thị báo cáo sức khỏe tổng hợp
    """
    print("-" * 20)
    print("Báo cáo sức khỏe")
    print("-" * 20)
    print(f"Tên: {ten}")
    print(f"Tuổi: {tuoi}")
    print(f"Chỉ số BMI: {bmi}")
    print(f"Lượng calo tiêu thụ: {calo_tieu_thu}")
    print("-" * 20)
    print("Hoạt động hàng ngày:")
    for ten_hoat_dong, thoi_gian in hoat_dong:
        print(f"- {ten_hoat_dong}: {thoi_gian} giờ")
    print("-" * 20)

