import sys
for lines in sys.stdin.readlines():
    n = int(lines)
    if n == 1:
        print('1')
    else:
        print(2*n-2)
