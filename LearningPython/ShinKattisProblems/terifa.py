x = int(input())

n = int(input())

total = x * (n+1)
used = 0
for i in range(n):
    used += int(input())

print(total-used)
