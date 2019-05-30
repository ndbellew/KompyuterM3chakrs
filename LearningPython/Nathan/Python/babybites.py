
def Successful():
    print("makes sense")

def Failure():
    print("something is fishy")

def Test(All_inputs):
    num = 0
    test_number = 0
    for i in All_inputs:
        num+=1
        test_number+=1
        if i == "mumble":
            if test_number != num:
                #print(i,num, test_number)
                return Failure()
        else:

            if int(i) != num:
                #print(i,num)
                return Failure()
    return Successful()

def main():
    Num_of_inputs = int(input())
    All_inputs = input().split()
    Test(All_inputs)

if __name__ == "__main__":
    main()
