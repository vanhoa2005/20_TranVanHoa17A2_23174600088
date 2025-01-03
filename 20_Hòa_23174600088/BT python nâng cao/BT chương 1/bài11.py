class TamGiac:
    def __init__(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Không phải là một tam giác")
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            super().__init__(a, b, c)
        else:
            raise ValueError("Không phải là tam giác vuông")

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        if a == b or a == c or b == c:
            super().__init__(a, b, c)
        else:
            raise ValueError("Không phải là tam giác cân")

class TamGiacDeu(TamGiacCan):
    def __init__(self, a):
        super().__init__(a, a, a)



