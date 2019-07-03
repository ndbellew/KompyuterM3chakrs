

##NOT SOLVED....

import math

def main():
    answer = []
    S = int(input())
    temp = ""
    if S % 2 != 0:
        temp = str(int(S/(2))+1) + ',' + str(int(S/2))
    else:
        temp = str(int(S/2)) + ',' + str(int(S/2))
    answer.append(temp)

    if S % 3 != 0:
        temp = str(int(S/3))




    for i in answer:
        print(i)

if __name__ == "__main__":
    main()
