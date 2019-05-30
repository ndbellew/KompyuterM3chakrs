Sequence_list=[]
#FAILURE
def increasing_x(x_multiplier, Starting_x):
    for i in Sequence_list:
        for k in range(0, Starting_x,1):
            for j in range(0, x_multiplier, 1):
                i[k]+=i[k]

def increasing_y(y_multiplier):
    pass

def main():
    parameters = input().split()
    Starting_x = int(parameters[1])
    Starting_y = int(parameters[0])
    x_multiplier = int(parameters[3])
    y_multiplier=int(parameters[2])
    for i in range(0, Starting_y, 1):
        Sequence_list.append(input())
    increasing_x(x_multiplier, Starting_x)
    increasing_y()
    for i in Sequence_list:
        print(i)


if __name__ == "__main__":
    main()
