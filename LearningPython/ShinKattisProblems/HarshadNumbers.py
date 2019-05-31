def findsmallest(x, line, sum, ans):
    while ans == 0:
        x += 1
        line = list(str(x))
        for i in range(len(line)):
            line[i] = int(line[i])
        x = int(x)
        sum = 0
        for i in range(len(line)):
            sum += line[i]
        if x%sum == 0:
            return x

ans = 0
x = input()
line = list(x)
for i in range(len(line)):
    line[i] = int(line[i])
x = int(x)
sum = 0
for i in range(len(line)):
    sum += line[i]
if x%sum == 0:
    print(x)
else:
    print(findsmallest(x, line, sum, ans))
