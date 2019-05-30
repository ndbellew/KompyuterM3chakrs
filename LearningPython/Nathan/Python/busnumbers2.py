#use dictionary and keep track of numbers that work, it needs to be the sum of two numbers
def findans(x,l):
    while(True):
        for i in l:
            if i>x:
                pass
            elif x-i > 0 and x-i in l:
                for j in l:
                    if j>x:
                        pass
                    elif x-j > 0 and x-j in l and j != x-i and j!=i:
                        #print(j,i,x)
                        return x
                    elif x<2 or x==0:
                        return 0
                    else:
                        pass
            elif x<2 or x==0:
                return 0
            else:
                pass
        x-=1
def main():
    l = []
    for i in range(74):
        l.append(i*i*i)
    l.pop(0)
    #print(l)
    x = int(input())
    ans = findans(x,l)
    if ans == 0:
        print("none")
    else:
        print(ans)

if __name__=="__main__":
    main()
