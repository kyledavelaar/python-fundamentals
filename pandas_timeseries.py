import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from pandas import DataFrame, Series

now = datetime.now()
print(now)
print(now.year, now.day, '\n')

d = datetime(2022, 10, 30, 9, 22)
print(d, '\n')

d = now - timedelta(days=10)
print(d, '\n')

d = str(now)
print(d, '\n')
d = now.strftime('%Y/%m/%d')
print(d, '\n')

ds = ["2011-07-06 12:00:00", "2011-08-06 00:00:00"]
ds2 = pd.to_datetime(ds)
print(ds2, '\n')

ts = Series(
    np.random.standard_normal(6),
    index=pd.date_range('2011-03', periods=6)
)
print(ts, '\n')

# can select item from date
print(ts['2011-03-05'], '\n')

# can select multiple
print(ts['2011-03-02':'2011-03-04'], '\n')

# can select all in year or month, etc
print(ts['2011'], '\n')

# can do all the same for data frames as well
d = pd.date_range('2022-01', periods=12, freq='M')
df = DataFrame(
    np.random.standard_normal(12),
    index=d,
    columns=['random']
)
print(df.loc['2022-04'], '\n')

######################################################
## Time zones
######################################################

import pytz

zones = pytz.common_timezones[:5]
print(zones, '\n')

ny = pytz.timezone('America/New_York')
print(ny, '\n')

# date_range can accept a tz
dr = pd.date_range('2022-01-01', periods=10, tz='UTC')
print(dr, '\n')

d2 = dr.tz_convert('America/Los_Angeles')
print(d2, '\n')

######################################################
## Add time
######################################################

s = pd.Timestamp('2011-01-01 00:30')
s2 = s + pd.Timedelta(days=1)
print(s2, '\n')

p = pd.Period('2011', freq='Y-DEC')
print(p, '\n') # period here is an entire year jan-dec
print(p+5) # shift to 5 years later

######################################################
## Period Ranges
######################################################

# can use a period range as an index
periods = pd.period_range('2000-01-01', '2000-06-30', freq='M')
s = Series(
    np.random.standard_normal(6),
    index=periods
)
print(s, '\n')

######################################################
## Resample (like groupby for dates)
######################################################

# use resample to group dates by month and calculate mean of those groups
dates = pd.date_range('2001-01-01', periods=100)
ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)
print(ts, '\n')
# ME = month end, could also use month start
m = ts.resample('ME').mean()
print(m, '\n')


# can add period as well to not have days in dates
m = ts.resample('ME', kind="period").mean();
print(m, '\n')



# chunk by time (here minutes)
dates = pd.date_range('2000-01-01', periods=12, freq='min')
ts = pd.Series(np.random.standard_normal(len(dates)), index=dates)
print(ts, '\n')
# by default grouping is left inclusive, right exclusive by default so get values 0 to 4:59, and next would be 5 to 5:59
m = ts.resample('5min').sum()
print(m, '\n')
# can change label to point to left
m = ts.resample('5min', closed='right', label='left').sum()
print(m, '\n')












