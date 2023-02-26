from datetime import date, timedelta

dt = date.today()
x = dt - timedelta(1)
y = dt + timedelta(1)
print('Yesterday:', x)
print('Today:', dt)
print('Tomorrow:', y)