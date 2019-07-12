def main():
    for i in range(int(input())):
        imported = 0
        ary = list(map(int, input().split()))
        for i in range(len(ary)-1):
            if (ary[i]*2) < ary[i+1]:
                imported += ary[i+1]-ary[i]*2
        print(imported)
if __name__ == "__main__":
    main()
