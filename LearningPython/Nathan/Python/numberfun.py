import math
answerlist = []
def test_add(a, b, c):
    if a+b == c:
        answerlist.append("Possible")
    else:
        test_multi(a,b,c)

def test_multi(a, b, c):
    if a*b == c:
        answerlist.append("Possible")
    else:
        test_sub(a,b,c)

def test_sub(a, b, c):
    if a-b == c or b-a == c:
        answerlist.append("Possible")
    else:
        test_div(a,b,c)

def test_div(a, b, c):
    if a/b ==c or b/a == c:
        answerlist.append("Possible")
    else:
        answerlist.append("Impossible")


def main():
    N = int(input())
    for i in range(0,N,1):
        numbers = input()
        numbers = numbers.split()
        test_add(int(numbers[0]),int(numbers[1]), int(numbers[2]))
    for i in answerlist:
        print(i)

if __name__ == "__main__":
    main()
