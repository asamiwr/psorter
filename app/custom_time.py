from datetime import datetime, timedelta
from . import sort
import time


def check_time(time_to_sort):
    hour, minute = map(int, time_to_sort.split(":"))

    now = datetime.now()

    target = now.replace(
        hour=hour,
        minute=minute,
        second=0,
        microsecond=0
    )

    if target <= now:
        target += timedelta(days=1)

    seconds = (target - now).total_seconds()

    print(f"Sorting will start after {seconds:.0f} seconds")

    time.sleep(seconds)

    print("Sorting started...\n")
    sort.start_sorting()
    print("Done.")