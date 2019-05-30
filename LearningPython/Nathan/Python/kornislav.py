
def main():
    abcd = input().split()
    abcd = sorted(abcd, reverse=True)
    a = int(abcd[0])#largest base
    b = int(abcd[1])#smallest possible base
    c = int(abcd[2])#last cut through
    d = int(abcd[3]) #height
    baseMod = a%b
    base = a-baseMod
    print(base*d)

if __name__ == "__main__":
    main()
