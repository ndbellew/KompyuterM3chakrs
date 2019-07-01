
line = input().split()
x, y, z = int(line[0]), int(line[1]), int(line[2])

dif1 = y-x
dif2 = z-y
if dif1 > dif2:
    print(dif1-1)
else:
    print(dif2-1)
