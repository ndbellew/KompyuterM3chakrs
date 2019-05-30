#Too be added
def transpose(matrix, move):
    if move == 0:
        return [[matrix[i][j] for j in range(3, -1, -1)] for i in range(4)]
    elif move == 1:
        temp = matrix
        for i in range(4):
            k = 3
            for j in range(4):
                matrix[j][i] = temp[i][k]
                k -=1
        return matrix
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
    '''
    for i in range(4):
        for j in range(4):
            print(matrix[i][j], end=' ')
        print("")
    '''
    return matrix, move
def write_answer(matrix, move):
    matrix = transpose(matrix, move)
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
            added1 = True
            line.pop()
            line.insert(0, 0)
        while line[2] == 0 and allzero < 10:
            line.pop(2)
            line.insert(0, 0)
            allzero += 1
        if line[2] == line[1]:
            line[2] *= 2
            added2 = True
            line.pop(1)
            line.insert(0, 0)
        if line[3] == line[2] and added1 != True:
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
