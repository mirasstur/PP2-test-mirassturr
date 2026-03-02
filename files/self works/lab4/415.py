import datetime
from datetime import timedelta
line1 = input()
line2 = input()

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)        

def tms(line):
    parts = line.split()

    date_str = parts[0]
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")

    ut_time = parts[1].replace("UTC", "")
    sign = 1 if ut_time[0] == "+" else -1

    h,m = map(int, ut_time[1:].split(":"))
    delta = timedelta(hours=h, minutes=m)
    if sign == 1:
        utc_dt = dt - delta
    else:
        utc_dt = dt + delta
        
    return utc_dt

br_dt = tms(line1)
cur_dt = tms(line2)

if br_dt.month == 2 and br_dt.day == 29 and not(is_leap(cur_dt.year)):
    new_br = br_dt.replace(cur_dt.year, month=2, day=28)
else:
    new_br = br_dt.replace(year=cur_dt.year)

if new_br < cur_dt:
    newt_year = cur_dt.year + 1
    if br_dt.month == 2 and br_dt.day == 29 and not(is_leap(newt_year)):
        new_br = br_dt.replace(year=newt_year, month=2, day=28)
    else:
        new_br = br_dt.replace(year=newt_year)

diff = new_br - cur_dt
print(int(diff.total_seconds()//86400))
    
