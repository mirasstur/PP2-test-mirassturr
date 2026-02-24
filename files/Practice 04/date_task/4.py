from datetime import datetime, timedelta

date1 = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")
date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")


difference = abs(date1 - date2)
print(difference.total_seconds())