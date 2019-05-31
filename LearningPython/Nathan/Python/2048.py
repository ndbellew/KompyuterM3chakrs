import numpy as np

def splitvars(line):
    for x in line.split():
        yield int(x)

def left(matrix):
    pass

def right(matrix):
    pass

def up(matrix):
    pass

def down(matrix):
    pass

def printmatrix(matrix):
    for i in matrix:
        print(str(i[0])+" "+str(i[1])+" "+str(i[2])+" "+str(i[3]))

def main():
    line = input()
    a,b,c,d = splitvars(line)
    line = input()
    e,f,g,h = splitvars(line)
    line = input()
    i,j,k,l = splitvars(line)
    line = input()
    m,n,o,p = splitvars(line)
    move = int(input())
    matrix = [[a,b,c,d],[e,f,g,h],[i,j,k,l],[m,n,o,p]]

if __name__=="__main__":
    main()
