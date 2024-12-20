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






######
indicec = np
condition = nhiet_do>20
indicec = np.where(condition)
day_indicec = indicec[0]

days_above_20_separated = day_indicec+1
days_above_20_separated


chenh_lech = ngay_sau - ngay_truoc

dff_max = np.arange(np.abs(chenh_lech)) + 1 
max_chenh_lech = chenh_lech[dff_max]

print("Chênh lệch nhiệt độ cao nhất là : ",max_chenh_lech)\
print("Ngày chênh lệch cao nhất ",dff_max)




