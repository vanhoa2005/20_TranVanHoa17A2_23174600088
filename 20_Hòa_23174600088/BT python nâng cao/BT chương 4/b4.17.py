import pandas as pd

ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])

ser_timeseries = pd.to_datetime(ser)

print("Series chuỗi thời gian:")
print(ser_timeseries)
