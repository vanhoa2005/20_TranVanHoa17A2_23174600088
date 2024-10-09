class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def kiem_tra_hop_le(self):
        return self.mau_so != 0

    def nhap_phan_so(self):
        while True:
            try:
                self.tu_so = int(input("Nhập tử số: "))
                self.mau_so = int(input("Nhập mẫu số: "))
                if self.kiem_tra_hop_le():
                    break
                else:
                    print("Mẫu số phải khác 0. Vui lòng nhập lại.")
            except ValueError:
                print("Vui lòng nhập số nguyên.")

    def in_phan_so(self):
        if self.mau_so == 1:
            print(self.tu_so)
        else:
            print(f"{self.tu_so}/{self.mau_so}")

ps1 = PhanSo()
ps1.nhap_phan_so()
print("Phân số vừa nhập là:")
ps1.in_phan_so()