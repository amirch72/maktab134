from datetime import time, date, datetime, timedelta


# new_datetime = datetime(1990, 2, 21)
# print(type(new_datetime))
# print(new_datetime)
# now_datetime = datetime.now()
# print(now_datetime)

# print(type(now_datetime - new_datetime))
# print((now_datetime - new_datetime).days)
# days_of_user = (now_datetime - new_datetime).days

# year = days_of_user // 365
# month = (days_of_user - year * 365) // 30
# day = days_of_user - (year * 365 + month * 30)

# print(year, month, day)

new_date = date(1980, 8, 19)
print(new_date)


delta = timedelta(weeks=3)
print(delta.total_seconds())

print(new_date - delta)


# %y => year in 2 digit
# %Y => yeat in 4 digits
# %m => month
# %h => month in words
# %d => day
# %H => hour
# %S => second