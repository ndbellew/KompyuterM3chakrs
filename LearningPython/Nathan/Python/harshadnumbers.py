def main(n):
    h = list(n)
    total = 0
    for i in h:
        total += int(i)
    if int(n) %total != 0:
        main(str(int(n)+1))
    else:
        print(n)

main(input())
