import numpy as np
# Tạo mảng nhiệt độ ngẫu nhiên với 30 ngày
np.random.seed(42)  # Để đảm bảo kết quả có thể tái tạo lại
nhiet_do = np.random.uniform(18, 35, 30)

# Làm tròn đến 2 chữ số sau dấu phẩy
nhiet_do = np.round(nhiet_do, 2)

print(nhiet_do)
# Tính nhiệt độ trung bình
nhiet_do_trung_binh = np.mean(nhiet_do)
print("Nhiệt độ trung bình trong tháng:", nhiet_do_trung_binh, "độ C")











