#!/usr/bin/env python3
from datetime import datetime, date
import pytz

tz_NY = pytz.timezone('Asia/Kolkata')
datetime_NY = str(datetime.now(tz_NY))

print(f"len(str(datetime_NY)): {len(datetime_NY)}")
print(f"\n\ndate.today(): {date.today()}\n\ndate: {datetime_NY[:10]}\n\ntime: {(datetime_NY[10:26]).lstrip()}")
