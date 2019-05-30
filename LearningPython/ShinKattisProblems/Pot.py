def main():
    n = int(input())
    list = []
    power = []
    for i in range(n):
        list.append(int(input()))
        power.append(int(round(list[i]%10)))
        list[i] = (int(round((list[i] / 10) - ((list[i]%10)/10))))
    ans = 0

    for i in range(2, n+2):
        ans += list[i-2]**power[i-2]
    print(ans)
if __name__ == "__main__":
    main()
'''
5
23
17
43
52
22

3
213
102
45

'''
