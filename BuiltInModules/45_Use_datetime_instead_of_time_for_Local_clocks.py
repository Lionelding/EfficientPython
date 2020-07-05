# Item 45: Use `datetime` instead of `time` for Local Clocks
"""
1. Avoid using the `time` module for translating between time zones
2. Use the `datetime` module and the `pytz` module to convert between time zones
3. Always represent the time in UTC and then do local time conversion. 
"""

from time import localtime, strftime
from time import mktime, strptime

from datetime import datetime, timezone

print('######### Example 1 #########')
## Example 1: `time` module

### Convert a UNIX timestamp to a local time
now = 1407694710
local_tuple = localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = strftime(time_format, local_tuple)
print(time_str)

### Convert a local time to a UNIX timestamp
time_tuple = strptime(time_str, time_format)
utc_now = mktime(time_tuple)
print(utc_now)

### Time Xone Convertion
parse_format = '%Y-%m-%d %H:%M:%S %Z'
depart_sfo = '2014-08-10 14:18:30 PDT'
try:
	time_tuple = strptime(depart_sfo, parse_format)
	time_str = strftime(time_format, time_tuple)
	print(time_str)
except ValueError as e:
	print(e)
	print('switching PDT to EDT will fix this')

print('######### Example 2 #########')
## Example 2: `datetime` module

### Convert a UNIX timestamp to a local time
now = datetime(2020, 7, 5, 19, 27, 30)
now_utc = now.replace(tzinfo=timezone.utc)
now_local = now_utc.astimezone()
print(f'local: {now_local}')

### Convert a local time to a UNIX timestamp
time_str = '2020-07-05 19:30:30'
now = datetime.strptime(time_str, time_format)
time_tuple = now.timetuple()
utc_now = mktime(time_tuple)
print(f'utc: {utc_now}')
