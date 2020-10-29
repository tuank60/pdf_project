import pandas as pd
import numpy as np
import time
# import ujson
from datetime import date, datetime, timedelta, timezone
# from datetime import datetime,timezone
# from pytz import timezone
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
# print(df2)
data = []
for i in range(1,10):
    # print(i)
    obj={}
    obj['mssv'] = 2015 * 10 + i
    obj['name TT00'] = "DOANHTUAN" + str(i%5)
    obj['datetime'] = datetime.utcnow()
    data.append(obj)
# print(obj)
df = pd.DataFrame(data)
print(df)
print(df['mssv'])
print(df.loc[df['mssv'] > 20155])
print(df.groupby("name TT00")['mssv'].sum().reset_index())
print(datetime.now())
print(datetime.now(timezone.utc))
print(datetime.now(timezone.utc).astimezone().tzinfo)
LOCAL_TIMEZONE = datetime.now(timezone.utc).astimezone().tzinfo
print(pd.to_datetime(df['datetime'], unit='s').dt.tz_localize('UTC').dt.tz_convert(LOCAL_TIMEZONE))
# print(pd.read_fwf(df['mssv']))