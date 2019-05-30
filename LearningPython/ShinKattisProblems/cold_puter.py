def main():

    twoD = [[11, 11],
            [4, 4],
            [3, 3],
            [20, 2],
            [10, 10],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [14, 0]]
    n, abc = input().split()
    n = int(n)
    result = 0
    for i in range(0, 4*n):
        line = input()
        if line[0] == "A":
            a = 0
        elif line[0] == "K":
            a = 1
        elif line[0] == "Q":
            a = 2
        elif line[0] == "J":
            a = 3
        elif line[0] == "T":
            a = 4
        else:
            try:
                a = int(line[0])
            except:
                a = 7
        if line[1] == "S":
            b = 0
        else:
            b = 1
        result += twoD[a][b]
    print(result)
if __name__ == "__main__":
  main()
