


n=0    
while n != -1:
    n = int(input())
    if n != -1:
        speed = []
        time = []
        for i in range(n):
            x, y = input().split()
            x = int(x)
            y = int(y)
            speed.append(x)
            time.append(y)
        ans = 0
        ti = 0
        for i in range(0, n):
            ans += speed[i]*(time[i]-ti)
            ti = time[i]
        print(ans, "miles")
'''
20 * 2 + 30 * 4
4
15 1
25 2
30 3
10 5
-1

'''
