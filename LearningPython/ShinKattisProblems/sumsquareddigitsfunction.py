#don't understand how this works actually
def main():
    for i in range(int(input())):
        ssd = 0
        k, b ,n = list(map(int,input().split()))
        while n > 0:
            ssd += (n%b) * (n%b)
            n = int(n/b)
        print(str(k) + " " + str(ssd))
if __name__ == "__main__":
    main()
