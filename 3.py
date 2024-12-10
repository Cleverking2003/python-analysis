import re
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

res = []

with open("lab_works_files/n_log2.txt") as f:
    for l in f:
        info = re.search(r"^(\d\d:\d\d:\d\d).*B00000000004 <--->.*KEEP.*pressure=([0-9.]+).*gard=([0-9.]+)", l)
        if info:
            res.append(info.groups())

prev_time = datetime.strptime("15:00:00", "%H:%M:%S")
times = []
press = []
guard = []
avg_press = 0
avg_guard = 0
i = 0
j = 0

for t, pr, g in res:
    time = datetime.strptime(t, "%H:%M:%S")
    diff = time - prev_time
    if diff.total_seconds() > 60 * 10:
        times.append(str(prev_time.time()))
        prev_time += timedelta(minutes=10)
        press.append(avg_press / i)
        guard.append(avg_guard / j)
        avg_guard = 0
        avg_press = 0
        i = 0
        j = 0
    avg_guard += float(g)
    avg_press += float(pr)
    i += 1
    j += 1

plt.xlabel('Время')
plt.ylabel('Давление')
plt.plot(times, press, label='B00000000004')
plt.legend()
plt.show()
plt.xlabel('Время')
plt.ylabel('gard')
plt.plot(times, guard, label='B00000000004')
plt.legend()
plt.show()
