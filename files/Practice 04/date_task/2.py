from datetime import datetime, timedelta

now = datetime.now()
print(now - timedelta(days = 1))
print(now)
print(now + timedelta(days = 1))

b = "banana"
print(b[:3])