
def MakeitString(a,b):
    return str(a)+","+str(b)

def printAnswer(someList):
    for i in someList:
        print(i)

def calc_Stars(Number_Of_Stars):
    number_set = []
    Final_Number=0
    if Number_Of_Stars%2 == 0:
        Final_Number = int(Number_Of_Stars/2)
        Final_String = MakeitString(Final_Number,Final_Number)
    else:
        Final_Number = int(Number_Of_Stars/2)
        Final_String= MakeitString(Final_Number+1, Final_Number)
    for i in range(2, Number_Of_Stars, 1):
        j=i-1
        k=i+j
        if Number_Of_Stars%k == i or Number_Of_Stars%k == 0:
            number_set.append(MakeitString(i,j))
        if Number_Of_Stars%(i+i) == i or Number_Of_Stars%(i+i) ==0:
            number_set.append(MakeitString(i,i))
    if Final_String not in number_set:
        number_set.append(Final_String)
    printAnswer(number_set)

def main():
    Number_Of_Stars = int(input())
    print(str(Number_Of_Stars)+":")
    calc_Stars(Number_Of_Stars)


if __name__=="__main__":
    main()
