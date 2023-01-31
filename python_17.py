# import datetime - import everything
from datetime import date
from datetime import time
from datetime import datetime
from datetime import datetime, timedelta
# timedelta is used to perform operation on datetime

# ----------------------------------------------------

date1 = date(2021, 11, 3)  # create date object
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)

current = date.today()
print(current)

str1 = date.isoformat(current)  # format to string
print(str1[0:2])

# ----------------------------------------------------

time1 = time(11, 30, 20)  # create time object
print(time1)
print(time1.hour)
print(time1.minute)
print(time1.second)
print(time1.microsecond)
time1 = time(11, 30, 20, 243)
print(time1)

str1 = time1.isoformat()  # format to string
print(str1)

# ----------------------------------------------------

date1 = datetime(2021, 4, 23, 12, 46, 20, 23)  # create datetime object
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)
print(date1.hour)
print(date1.minute)
print(date1.second)
print(date1.microsecond)

current = datetime.now()
print(current)

str1 = datetime.isoformat(current)  # format to string
print(str1)

# ----------------------------------------------------

timestamp = datetime.fromtimestamp(1212121212)
print(timestamp)


date1 = datetime(2021, 4, 23, 12, 46, 20, 23)
print(date1)

new_date = date1+timedelta(hours=5)
print(new_date)
