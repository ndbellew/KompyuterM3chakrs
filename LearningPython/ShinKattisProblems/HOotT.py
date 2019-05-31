L, n = input().split()
L = int(L)
n = int(n)

c = 0
rejected = 0
for i in range(n):
    state, num = input().split()
    num = int(num)
    if state == "enter" and L >= (num+c):
        c += num
    elif state == "leave":
        c -= num
    else:
        rejected += 1

print(rejected)
