import datetime
from datetime import timedelta

# %a = weekday(short)
# %A = weekday(full)
# %b = month name(short)
# %B = month name(full)
# %y = year(short)
# %Y = year(full)
# %d = day
# %H = hour(00-23)
# %I = hour(00-12)
# %S = second
# %f = microsecond
# %p = AM/PM


POSTED_DATE = datetime.date.today()

time = datetime.datetime.now()

POSTED_TIME = time.strftime("%I.%M %p")

replydate = datetime.datetime.now() + timedelta(days=2)

DATE_OF_REPLY = replydate.strftime("%Y-%m-%d")

CAPTCHA_DATE = datetime.datetime.now() + timedelta(seconds=1)
