import operator
def main():
    dict = {}
    for i in range(int(input())):
        temp = input().split()
        try:
            temp[0], temp[1] = temp[1], int(temp[0])/2
        except:
            pass
        dict.update( {temp[0] : int(temp[1])} )
    dict = sorted(dict.items(), key=operator.itemgetter(1))
    for i in range(len(dict)):
        print(dict[i][0])
if __name__ == "__main__":
    main()
