class TS:
    def __init__(self, hoTen, toan, ly, hoa):
        self.hoTen = hoTen
        self.toan = toan
        self.ly = ly
        self.hoa = hoa

    def nhapThongTin(self):
        self.hoTen = input("Nhập họ tên thí sinh: ")
        self.toan = float(input("Nhập điểm Toán: "))
        self.ly = float(input("Nhập điểm Lý: "))
        self.hoa = float(input("Nhập điểm Hóa: "))

    def inThongTin(self):
        print("Họ tên:", self.hoTen)
        print("Điểm Toán:", self.toan)
        print("Điểm Lý:", self.ly)
        print("Điểm Hóa:", self.hoa)
        print("Tổng điểm:", self.tinhTongDiem())

    def tinhTongDiem(self):
        return self.toan + self.ly + self.hoa
    

def nhapDanhSachThiSinh():
    danhSach = []
    n = int(input("Nhập số lượng thí sinh: "))
    for i in range(n):
        ts = TS("", 0, 0, 0)
        ts.nhapThongTin()
        danhSach.append(ts)
    return danhSach

def sapXepVaInDanhSachTrungTuyen(danhSach):
    # Sắp xếp theo tổng điểm giảm dần
    danhSach.sort(key=lambda x: x.tinhTongDiem(), reverse=True)

    # In danh sách trúng tuyển (điểm chuẩn = 20)
    print("Danh sách thí sinh trúng tuyển:")
    for ts in danhSach:
        if ts.tinhTongDiem() >= 20:
            ts.inThongTin()


danhSach = nhapDanhSachThiSinh()
sapXepVaInDanhSachTrungTuyen(danhSach)