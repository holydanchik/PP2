from datetime import datetime

today = datetime.today()
birthday = datetime(datetime.today().year,6,23)

if birthday<today:
    birthday = datetime(datetime.today().year+1,6,23)

until_birthday = birthday - today

print(round(until_birthday.total_seconds()))
