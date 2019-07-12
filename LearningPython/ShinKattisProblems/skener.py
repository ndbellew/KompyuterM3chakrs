def multiplier(n, string):
    return ''.join([x*n for x in string])

def main():
    lines = []
    R, C, Zr, Zc = list(map(int, input().split()))
    for i in range(R):
        lines.append(input())

    print(lines)
    for i in range(R):
        multiplier(Zc, lines[R])





if __name__ == "__main__":
    main()

#   C
#R
