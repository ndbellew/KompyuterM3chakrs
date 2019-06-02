x, y = input().split()
a = list(x)
b = list(y)
x = int(x)
y = int(y)
xx = [int(a[0]), int(a[1]), int(a[2])]
yy = [int(b[0]), int(b[1]), int(b[2])]

def reverse(num):
    rev = 0
    while num > 0:
        rev = (10*rev) + num%10
        num //= 10
    return rev

if xx[2] > yy[2]:
    print(int(reverse(x)))
elif yy[2] > xx[2]:
    print(int(reverse(y)))
else:
    if xx[1] > yy[1]:
        print(int(reverse(x)))
    elif yy[1] > xx[1]:
        print(int(reverse(y)))
    else:
        if x[0] > yy[0]:
            print(int(reverse(x)))
        elif yy[0] > xx[0]:
            print(int(reverse(y)))
        else:
            print(int(reverse(x)))
