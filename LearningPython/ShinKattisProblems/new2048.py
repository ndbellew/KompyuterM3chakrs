import copy
def transpose(matrix, move):
    temp = copy.deepcopy(matrix)
    if move == 0:
        return [[matrix[i][j] for j in range(3, -1, -1)] for i in range(4)]
    elif move == 1:
        for i in range(4):
            k = 3
            for j in range(4):
                matrix[i][j] = temp[k][i]
                k -=1
        return matrix
    elif move == 3:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    else:
        return matrix
def transpose_back(matrix, move):
    if move == 0:
        return transpose(matrix, move)
    elif move == 1:
        return transpose(transpose(transpose(matrix, move), move), move)
    elif move == 3:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    else:
        return matrix
def string_to_int(line):
    return [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
def read_data():
    matrix = []
    for i in range(4):
        matrix.append(string_to_int(input().split()))
    move = int(input())
    matrix = transpose(matrix, move)
    return matrix, move
def write_answer(matrix, move):
    matrix = transpose_back(matrix, move)
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=' ')
        print("")
def move_matrix(matrix):
    for i in range(4):
        added1 = False
        added2 = False
        allzero = 0
        line = matrix[i]
        while line[3] == 0 and allzero < 10:
            line = [line[-1]] + line[:-1]
            allzero += 1
        if line[3] == line[2]:
            line[2] *= 2
            added2 = True
            line.pop()
            line.insert(0, 0)
        while line[2] == 0 and allzero < 10:
            line.pop(2)
            line.insert(0, 0)
            allzero += 1
        if line[2] == line[1] and added1 != True:
            line[2] *= 2
            added2 = True
            line.pop(1)
            line.insert(0, 0)
        if line[3] == line[2] and added2 != True:
            line[2] *= 2
            added2 = True
            line.pop()
            line.insert(0, 0)
        if line[1] == line[0]:
            line[1] *= 2
            line[0] = 0
        matrix[i] = line
    return matrix
def main():
    # 0 - Left, 1 - Up, 2 - Right, 3- Down
    matrix, move = read_data()
    move_matrix(matrix)
    write_answer(matrix, move)
if __name__ == "__main__":
    main()



'''
GO
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
0
4 0 0 0
4 16 8 2
2 64 32 4
2048 64 0 0
GO
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
1
2 16 8 4
4 64 32 4
2 1024 64 0
1024 0 0 0
GO
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
2
0 0 0 4
4 16 8 2
2 64 32 4
0 0 2048 64

GOOD
2 0 0 2
4 16 8 2
2 64 32 4
1024 1024 64 0
3
2 0 0 0
4 16 8 0
2 64 32 4
1024 1024 64 4

GOOD
2 2 4 8
4 0 4 4
16 16 16 16
32 16 16 32
0
4 4 8 0
8 4 0 0
32 32 0 0
32 32 32 0

GOOD
2 2 4 8
4 0 4 4
16 16 16 16
32 16 16 32
2
0 4 4 8
0 0 4 8
0 0 32 32
0 32 32 32
'''
