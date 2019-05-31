
def main():
    count = 0
    cardlist=[]
    cardtypes = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    templist=[]
    hand = input().split()
    for card in hand:
        if card[0]==1:
            cardlist.append(str(10))
        else:
            cardlist.append(card[0])
    for i in cardtypes:
        x = cardlist.count(i)
        templist.append(x)
    templist = sorted(templist)
    print(templist[-1])


if __name__=="__main__":
    main()


#FAILURE
#How did we fail?
