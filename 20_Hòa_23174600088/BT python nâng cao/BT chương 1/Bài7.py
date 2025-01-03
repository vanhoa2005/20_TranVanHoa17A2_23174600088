class Date:
    def __init__(self, day=1, month=1, year=2000):
        """
        Khởi tạo một đối tượng Date.

        Args:
            day (int, optional): Ngày trong tháng. Defaults to 1.
            month (int, optional): Tháng trong năm. Defaults to 1.
            year (int, optional): Năm. Defaults to 2000.
        """
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        """In thông tin về ngày ra màn hình."""
        print(f"{self.day}/{self.month}/{self.year}")

    def next_day(self):
        """Tính ngày tiếp theo."""
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and self.is_leap_year():
            days_in_month[1] = 29

        self.day += 1
        if self.day > days_in_month[self.month - 1]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1

    def is_leap_year(self):
        """Kiểm tra xem năm có phải là năm nhuận không."""
        return (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)



# Tạo một đối tượng Date với ngày mặc định
date1 = Date()
date1.display()  # In ra: 1/1/2000

# Tạo một đối tượng Date với ngày cụ thể
date2 = Date(29, 2, 2024)
date2.display()  # In ra: 29/2/2024

# Tính ngày tiếp theo của date2
date2.next_day()
date2.display()  # In ra: 1/3/2024