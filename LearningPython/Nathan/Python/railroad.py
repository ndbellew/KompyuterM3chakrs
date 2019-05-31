
def main():
    xy = input().split()
    x = int(xy[0])
    y = int(xy[1])
    if not y%2==0:
        return "impossible"
    else:
        return "possible"


if __name__=="__main__":
    ans = main()
    print(ans)
