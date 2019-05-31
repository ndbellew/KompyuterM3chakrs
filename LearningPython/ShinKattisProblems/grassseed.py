cost = float(input())
lawns = int(input())
sum = 0
for i in range(lawns):
    a, b = input().split()
    a = float(a)
    b = float(b)
    sum += (a*b)*cost

print('{0:.8f}'.format(sum))
