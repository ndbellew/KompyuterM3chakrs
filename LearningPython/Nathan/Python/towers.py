import math
PowerDict = {}
alist = []
def Evaluate_Expression(expression):
    pass

def main():
    number_of_cases = int(input())
    for i in range(0,number_of_cases,1):
        expression = input()
        exp_as_func = eval('lambda: '+ expression.replace('^','**'))
        value = exp_as_func()
        PowerDict[expression]=value

    sorted_dict = [(k, PowerDict[k]) for k in sorted(PowerDict, key=PowerDict.get, reverse=False)]

    print("Case 1:")
    for k, v in sorted_dict:
        print(k)


if __name__=="__main__":
    main()
