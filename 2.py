from datetime import datetime
import re

def function(string):
    return len(re.findall(r"\b[ОоЭэ]", string))

print(function('Сказала Ольга: "Это верно ,что 2+2=4"'))

def function2(string):
    return len(re.findall(r"\b[a-zA-Zа-яА-я\-]+", string))

def function3(string):
    return len(re.findall(r"\b[А-Я]{2,}\b", string))


def function4(dt1, dt2):
    d1 = datetime.strptime(dt1, '%Y%m%d %H:%M:%S')
    d2 = datetime.strptime(dt2, '%Y%m%d %H:%M:%S')
    
    if d2 > d1:
        return int((d2 - d1).total_seconds() // 3600)
    return int((d1 - d2).total_seconds() // 3600)

print(function4("20211212 12:12:12", "20211212 11:12:12"))
print(function4("20211212 12:12:12", "20211213 12:13:13"))

def function5(string):
    res = re.findall(r"^[a-z]*", string) + re.findall(r"[A-Z][a-z]*", string)
    print(res)
    return '_'.join([x.lower() for x in res])

print(function5("camelCaseVar"))
print(function5("myWonderfulVar"))

# with open("lab_works_files/n_log1.txt") as f:
#     out = open("out1.txt", 'w+')
#     for line in f:
#         mat = re.search(r"KEEP.*pressure=(\d+)", line)
#         if (mat):
#             out.write(mat.group(1) + "\n")

import math

mi = 1_000_000_000
ma = 0
avg = 0.
count = 0

with open("out1.txt") as f:
    for line in f:
        num = int(line)
        mi = min(mi, num)
        ma = max(ma, num)
        avg += num
        count += 1

avg /= count
print(count, mi, ma, avg)
print(mi + ma + int(avg))
