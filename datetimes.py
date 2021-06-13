from datetime import date
now = date.today()
print(now)

birthday = date(1999, 2, 12)
age = now - birthday
print(age.days)
year = age.days/365
print(year)