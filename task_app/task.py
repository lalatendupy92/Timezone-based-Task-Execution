from datetime import datetime, date, timedelta, timezone
from pytz import timezone, country_timezones, country_names

country_codes = {country: code for code, country in country_names.items()}

task_type = input('Enter task:')
country = input('Enter country:')
email_start_time = '19:00:00'
email_end_time = '21:00:00'
call_start_time = '13:00:00'
call_end_time = '14:30:00'
sms_start_time = '10:00:00'
sms_end_time = '17:00:00'

if task_type == 'email' and country == 'India':
    start_time = email_start_time
    end_time = email_end_time

elif task_type == 'call' and country == 'India':
    start_time = call_start_time
    end_time = call_end_time
elif task_type == 'sms' and country == 'India':
    start_time = sms_start_time
    end_time = sms_end_time
elif task_type == 'call' and country == 'United States':
    start_time = call_start_time
    end_time = call_end_time
elif task_type == 'email' and country == 'United States':
    start_time = email_start_time
    end_time = email_end_time
elif task_type == 'sms' and country == 'United States':
    start_time = sms_start_time
    end_time = sms_end_time
elif task_type == 'call' and country == 'Japan':
    start_time = call_start_time
    end_time = call_end_time
elif task_type == 'email' and country == 'Japan':
    start_time = email_start_time
    end_time = email_end_time
elif task_type == 'sms' and country == 'Japan':
    start_time = sms_start_time
    end_time = sms_end_time
elif task_type == 'call' and country == 'Germany':
    start_time = call_start_time
    end_time = call_end_time
elif task_type == 'email' and country == 'Germany':
    start_time = email_start_time
    end_time = email_end_time
elif task_type == 'sms' and country == 'Germany':
    start_time = sms_start_time
    end_time = sms_end_time
elif task_type == 'call' and country == 'Australia':
    start_time = call_start_time
    end_time = call_end_time
elif task_type == 'sms' and country == 'Australia':
    start_time = sms_start_time
    end_time = sms_end_time

tz = country_timezones[country_codes[country]]

current_time = str(datetime.now().astimezone(timezone(tz[0])).time())
day = datetime.now().astimezone(timezone(tz[0])).strftime('%A')

try:
    if start_time <= current_time <= end_time and (day == 'Tuesday' or day == 'Thursday'):
        print(True)
    elif day in ["Monday", "Friday", "Saturday", "Sunday"]:
        print(start_time, 'Tuesday')
    elif day == 'Wednesday':
        print(start_time, 'Thursday')
    else:
        print(False)
except:
    print('data not available')
