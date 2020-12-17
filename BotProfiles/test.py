import random

count = ""
count2 = ""
dates = []
for i in range(1,13):
    if i < 10:
        count = f"0{i}"
    else:
        count = str(i)
    for j in range(20,31):
        count2 = str(j)
        dates.append(f"{count} / {count2},")

all = ""
for date in dates:
    all += date
print(all)