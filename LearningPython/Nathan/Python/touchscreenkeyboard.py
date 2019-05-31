#! /bin/python3
row1 = list("qwertyuiop")
row2 = list("asdfghjkl")
row3 = list("zxcvbnm")
answerlist = []

def check_row_pos(node, column):#return what position inside the row it is
    length = 0
    if column == 1:
        length = len(row1)
    else if column == 2:
        length = len(row2)
    else:
        length = len(row3)
    for i in range(0,length,1):
        if

def check_column_pos(node):#return row it is in.
    if node in row1:
        return (1)
    else if node in row2:
        return (2)
    else:
        return (3)

def solve(root,node):
    node_column,root_column,count,column_difference,row_difference  = 0,0,0,0,0
    root_row,node_row = 100,100
    for i in range(0,len(root),1):
        node_column = check_column_pos(node[i])
        node_row = check_row_pos(node[i],node_column)
        root_column = check_column_pos(root[i])
        root_row = check_row_pos(root[i], node_column)

        column_difference = abs(node_column-root_column)
        if not column_difference == 0:
            count+=column_difference
        node_column = root_column

        row_difference= abs(node_row - root_row)
        if not row_difference == 0:
            count+=row_difference
        node_row = root_row
        """
        incomplete needs to be in a tuple and then sort each individual tuple and print it out like its in list
        look this up when not busy
        """

    answerlist.append(node+" "+str(count))

def main():
    testCases = int(input())
    for i in range(0,testCases,1):
        root_test = input().split()
        root = root_test[0]
        test = int(root_test[1])
        for i in range(0,test,1):
            solve(root,input())

if __name__ == "__main__":
    main()

"""
the way its calculated is the top row has 10 characters the the second has 9 and the last has 7
so you move down from your current spot is one move but it goes to the exact same spot in one row as the other
so if you move from a to c you go to row1[0] to row2[0] and then move over two more to c
"""
