#!/usr/bin/python3
import string
lista = []
listb = []
alpha = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
alpha_list = list(string.ascii_uppercase)

def divide(Message):
    length = len(Message)
    for i in range(0,int(length/2),1):
        lista.append(Message[i])
    for i in range(int(length/2),length,1):
        listb.append(Message[i])

def rotate():
    first_list = []
    second_list = []
    score,temp = 0,0
    for i in lista:
        score += alpha[i]
        if score>25:
            score-=25
    for i in lista:
        temp = (score + alpha[i])-2
        if temp>25:
            temp-=25
        first_list.append(alpha_list[temp])
    print(score)
    alist = first_list
    score,temp = 0,0
    for i in listb:
        score += alpha[i]
        if score>25:
            score-=25
    for i in listb:
        temp = (score + alpha[i])-2
        if temp>25:
            temp-=25
        second_list.append(alpha_list[temp])
    blist = second_list
    print(alist,blist)

def merge():
    score,temp = 0,0
    other_list,temp_list,new_value = [],[]
    for i in blist:
        temp_list.append(alpha[i])
    for i in alist:
        other_list.append(alpha[i])
    for i in range(0,len(temp_list),1:
        temp = temp_list[i]+other_list[i]
        while temp>25:
            temp-=25

        new_value.append()


def main():
    Message = list(input())
    divide(Message)
    rotate()


    #print(lista,listb)


if __name__ == "__main__":
    main()
