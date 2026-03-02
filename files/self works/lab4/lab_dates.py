import datetime
from datetime import timedelta
line1 = input()
line2 = input()
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

utc_dt1 = tms(line1)
utc_dt2 = tms(line2)

diff = abs(utc_dt1 - utc_dt2)
print(int(diff.total_seconds()//86400))