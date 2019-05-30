import math
answerlist = []

def main():
    T = int(input())
    for i in range(T):
        x = int(input())
        ans = str(math.factorial(x))
        answerlist.append(ans[-1])

    for i in answerlist:
        print(i)

if __name__=="__main__":
    main()
