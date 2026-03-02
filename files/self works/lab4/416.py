import datetime
from datetime import timedelta
line1 = input()
line2 = input()

def tms(line):
    parts = line.split()

    date_str = parts[0] + " " + parts[1]
    dt = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    
    ut_time = parts[2].replace("UTC", "")
    sign = 1 if ut_time[0] == "+" else -1

    h,m = map(int, ut_time[1:].split(":"))
    delta = timedelta(hours=h, minutes=m)
    if sign == 1:
        utc_dt = dt - delta
    else:
        utc_dt = dt + delta
        
    return utc_dt

start_tm = tms(line1)
end_tm = tms(line2)
diff = end_tm - start_tm
print(int(diff.total_seconds()))
