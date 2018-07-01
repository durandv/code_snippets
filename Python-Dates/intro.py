import datetime
import pytz

d = datetime.date(2018, 6, 10)
td = datetime.date.today()

# print(d, td)
# print(td.day, td.weekday(), td.isoweekday())

tdelta = datetime.timedelta(days=7)

# print(td + tdelta)

bday = datetime.date(2018, 9, 9)

till_day = bday - td
# print(till_day)

t = datetime.time(9, 30, 45, 10000)
# print(t)
# print(t.hour)

dt = datetime.datetime(2018, 1, 1, 9, 30, 45, 10000)
# print(dt)
# print(dt.date())

tdelta = datetime.timedelta(days=7)
# print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# PYTZ
# dt = datetime.datetime(2018, 6, 10, 20, 18, 0, 0, tzinfo=pytz.UTC)
# print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

dt_mnt = dt_now.astimezone(pytz.timezone('America/Argentina/Buenos_Aires'))
# print(dt_mnt)

# print(pytz.all_timezones)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('America/Argentina/Buenos_Aires'))
print(dt_mnt.strftime('%B %d, %Y'))

dt_str = 'July 26, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)