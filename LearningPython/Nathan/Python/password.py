

def solve(passlist):
    ans = 0.0000
    for i in range(0, len(passlist),1):
        ans += (i+1)* passlist[i]
    return ans

def main():
    N = int(input())
    passlist = []
    for i in range(0,N,1):
        password = input().split()
        passlist.append(float(password[1]))

    ans = solve(sorted(passlist)[::-1])
    print(ans)

if __name__=="__main__":
    main()
