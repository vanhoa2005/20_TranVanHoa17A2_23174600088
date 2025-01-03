class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def nhap_du_lieu(self):
        self.dai = float(input("Nhập độ dài cạnh dài: "))
        self.rong = float(input("Nhập độ dài cạnh rộng: "))

    def tinh_chu_vi(self):
        return 2 * (self.dai + self.rong)

    def tinh_dien_tich(self):
        return self.dai * self.rong

    def in_thong_tin(self):
        print("Hình chữ nhật có:")
        print("Chiều dài:", self.dai)
        print("Chiều rộng:", self.rong)
        print("Chu vi:", self.tinh_chu_vi())
        print("Diện tích:", self.tinh_dien_tich())



hinh_chu_nhat = HinhChuNhat(0, 0)  
hinh_chu_nhat.nhap_du_lieu()
hinh_chu_nhat.in_thong_tin()