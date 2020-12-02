from collections import *

with open("puzzleinput_d2.txt") as f:
        a = f.read().strip().split("\n")

for x, ele in enumerate(a):
    a[x] = a[x].split()

count = 0

for x, ele in enumerate(a):
    
    if int(ele[0].split("-")[0]) <= (ele[-1].count(ele[1][0])) <= int(ele[0].split("-")[1]):
        count += 1
print("part 1", count)

count = 0

for x, ele in enumerate(a):
    x = int(ele[0].split("-")[0])
    y = int(ele[0].split("-")[1])
    
    if (x - 1 >= 0 and ele[-1][x-1] == ele[1][0]):
        if (y - 1 >= 0 and ele[-1][y-1] == ele[1][0]):
            pass
        else:
            count += 1
            continue
    if (y - 1 >= 0 and ele[-1][y-1] == ele[1][0]):
        if (x - 1 >= 0 and ele[-1][x-1] == ele[1][0]):
            pass
        else:
            count += 1
            continue
    
print("part 2", count)
