import datetime as dt

# get the current date and time
now = dt.datetime.now()
print(now)

# get current date
current_date = dt.date.today()
print(current_date)
print("Current year:", current_date.year)
print("Current month:",current_date.month)
print("Current day:", current_date.day)

#get custom date
d = dt.date(2024, 12, 25)
print(d)


from datetime import time

# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b= time(minute = 34,hour = 11, second = 56)
print(b)

# time(hour, minute, second, microsecond)
c= time(11, 34, 56, 234566)
print(c)


from datetime import datetime

# datetime(year, month, day)
a = datetime(2022, 12, 28)
print(a)


# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2022, 12, 28, 23, 55, 59, 342380)
print(b)

#print diff between two dates
from datetime import datetime
a=datetime(2025, 10,23)
print(a)
b=datetime(2002, 4,2)
print(b)
print(a-b)

