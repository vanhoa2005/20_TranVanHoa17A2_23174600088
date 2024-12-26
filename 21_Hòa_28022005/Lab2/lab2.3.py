import numpy as np

# 1. Đọc dữ liệu từ 2 tập tin efficiency.txt và shifts.txt
def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

efficiency = read_file('21_Hòa_28022005\Lab2\efficiency.txt')
shifts = read_file('21_Hòa_28022005\Lab2\shifts.txt')

# 2. Tạo numpy array np_shifts từ list shifts và kiểm tra kiểu dữ liệu
np_shifts = np.array(shifts, dtype='U10')
print(f"np_shifts dtype: {np_shifts.dtype}")

# 3. Tạo numpy array np_efficiency từ list efficiency và kiểm tra kiểu dữ liệu
np_efficiency = np.array(efficiency, dtype=float)
print(f"np_efficiency dtype: {np_efficiency.dtype}")

# 4. Tính hiệu suất sản xuất trung bình của những nhân viên làm việc vào ca 'Morning'
morning_mask = np_shifts == 'Morning'
morning_efficiency = np_efficiency[morning_mask]
morning_avg = morning_efficiency.mean() if morning_efficiency.size > 0 else 0
print(f"Hiệu suất trung bình ca 'Morning': {morning_avg:.2f}")

# 5. Tính hiệu suất sản xuất trung bình của những nhân viên làm việc trong các ca khác
non_morning_mask = np_shifts != 'Morning'
non_morning_efficiency = np_efficiency[non_morning_mask]
non_morning_avg = non_morning_efficiency.mean() if non_morning_efficiency.size > 0 else 0
print(f"Hiệu suất trung bình các ca khác: {non_morning_avg:.2f}")

# 6. Tạo mảng dữ liệu có cấu trúc workers
workers = np.zeros(len(np_shifts), dtype={'names': ('shift', 'efficiency'),
                                          'formats': ('U10', 'f4')})
workers['shift'] = np_shifts
workers['efficiency'] = np_efficiency

# 7. Sắp xếp mảng workers theo efficiency
workers_sorted = np.sort(workers, order='efficiency')

# Xác định ca làm việc có hiệu suất cao nhất và thấp nhất
highest_efficiency_shift = workers_sorted[-1]['shift']
lowest_efficiency_shift = workers_sorted[0]['shift']

print(f"Ca làm việc hiệu suất cao nhất: {highest_efficiency_shift}")
print(f"Ca làm việc hiệu suất thấp nhất: {lowest_efficiency_shift}")