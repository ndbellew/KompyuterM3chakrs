def main():
    answer = []

    n = int(input())
    for i in range(n):
        b, p = input().split()
        b = int(b)
        p = float(p)

        bpm = 60*b/p
        abpm = 60/p
        temp = [bpm-abpm, bpm, bpm+abpm]
        answer.append(temp)
    for i in range(0, n):
        print(round(answer[i][0],4), round(answer[i][1],4), round(answer[i][2],4))
if __name__ == "__main__":
    main()
