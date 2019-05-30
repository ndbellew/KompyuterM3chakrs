

line = input().split()
a, b, c = int(line[0]), int(line[1]), int(line[2])
size = (b**2+c**2)**0.5
ans = []
for i in range(a):
    num = int(input())
    if num <= size:
        ans.append("DA")
    else:
        ans.append("NE")
for x in ans:
    print(x)
