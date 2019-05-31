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
        twozero = False
        allzero = 0
        aa_a = False
        line = matrix[i]
        if line[1] == 0 and line[2] == 0 and line[0] != 0 and line[3] != 0:
            twozero = True
        if line[2] == 0 and line[0] == line[1] and line[0] == line[3]:
            aa_a = True
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
        if line[2] == line[1] and added1 != True and aa_a != True:
            line[2] *= 2
            added2 = True
            line.pop(1)
            line.insert(0, 0)
        while line[1] == 0 and allzero < 10:
            line.pop(1)
            line.insert(0, 0)
            allzero += 1
        if line[3] == line[2] and added2 != True:
            line[3] *= 2
            line.pop(2)
            line.insert(0, 0)
        elif twozero == True:
            line[3] *= 2
            line.pop(2)
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
