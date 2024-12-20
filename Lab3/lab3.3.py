import pandas as pd

# 1. Đọc file stocks2.csv vào DataFrame stocks2
stocks2 = pd.read_csv('21_Hòa_28022005\Lab3\stocks2.csv')

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
# Giả sử stocks1 đã được đọc trước đó
stocks1 = pd.read_csv('21_Hòa_28022005\Lab3\stocks1.csv')  # Nếu chưa đọc, bạn cần đọc file này trước
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks_avg = stocks.groupby('date')[['open', 'high', 'low', 'close']].mean()

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print(stocks_avg.head())
