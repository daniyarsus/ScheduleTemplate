import schedule
import time
from datetime import datetime, timedelta
import pytz

moscow_tz = pytz.timezone('Europe/Moscow')


def my_task():
    print("Task is completed!")


def job_with_timezone(hour, minute, task):
    now = datetime.now(moscow_tz)

    task_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if task_time < now:
        task_time = task_time + timedelta(days=1)

    time_until_task = (task_time - now).total_seconds()

    schedule.every().day.at(task_time.strftime("%H:%M")).do(task)

    time.sleep(time_until_task)
    task()


job_with_timezone(hour=18, minute=47, task=my_task)

while True:
    schedule.run_pending()
    time.sleep(1)
