a, b = input().split()
a = int(a)
b = int(b)
if a == 0 and b < 45:
    a = 23
    temp =  45-b
    b = 60 -temp
elif b < 45:
    temp = 45-b
    a -= 1
    b = 60 - temp
else:
    b -= 45
print(a, b)
