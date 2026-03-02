import datetime

x = datetime.datetime.now()
y = datetime.datetime.today()
print(x)

print(x.year)
print(x.strftime("%A"))


x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%B")) # print month name

