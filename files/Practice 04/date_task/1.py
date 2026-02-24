from datetime import datetime, timedelta
current_time = datetime.now()
specific_day = current_time - timedelta(days = 5)
print(specific_day)

