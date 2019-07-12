def main():
    count = 0
    final = []
    while True:
        answer = []
        index = 0 #index for insertion goes 0,1,1,2,2,3,3,4,4
        n = int(input())
        if n != 0:
            for i in range(n):
                answer.insert(index, input())
                if i%2 == 0:
                    index += 1
            count += 1
            answer.insert(0, ("SET " + str(count)))
        else:
            break
        final.append(answer)
    for i in range(len(final)):
        for x in final[i]:
            print(x)
if __name__ == "__main__":
    main()

"""
7
Bo
Pat
Jean
Kevin
Claude
William
Marybeth
Bo
6
Jim
Ben
Zoe
Joey
Frederick
Annabelle
5
John
Bill
Fran
Stan
Cece
0
"""
