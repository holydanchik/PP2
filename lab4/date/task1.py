from datetime import date, timedelta

dt = date.today()
x = dt - timedelta(5)
y = dt + timedelta(5)
print('date 5 days ago:', x)
print('date after 5 days:', y)