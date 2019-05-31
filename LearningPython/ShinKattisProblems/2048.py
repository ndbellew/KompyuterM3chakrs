def string_to_int(line):
    return [int(line[0]), int(line[1]), int(line[2]), int(line[3])]
def read_data():
    matrix = []
    #Assuming move == 0 or 2 # Horizonal Moves
    for i in range(4):
        matrix.append(string_to_int(input().split()))
    #Read move#
    move = int(input())
    return matrix, move
def write_answer(matrix, move):
    if move == 1:
        for i in range(4):
            for j in range(4):
                print(matrix[j][i], end=' ')
            print("")
    else:
        for i in range(4):
            for j in range(4):
                print(matrix[i][j], end=' ')
            print("")
def transpose(matrix, move):
    if move == 0:
        return [[matrix[i][j] for i in range(3, -1, -1)] for j in range(4)]
    elif move == 1:
        return [[matrix[i][j] for i in range(4)] for j in range(3, -1, -1)]
    elif move == 3:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

def action_to_right(line, act):
    if(act == 0):
        line = [0, 0, line[2]*2, line[3]*2]
    elif(act == 1):
        line = [0, 0, 0, sum(line)]
    else:
        while line[3] == 0:
            line[1:] + [line[0]]
        if line[3] == line[2]:
            line[2] *= 2
            line.pop()
            line.insert(0, 0)
    #[8 0 4 4]
    #[0 8 0 8] if line[2] == 0
        if line[2] == 0:
            line.pop(line[2])
            line = [0] + line


    return line
def action_to_left(line, act):
    if(act == 0):
        line = [line[0]*2, line[1]*2, 0, 0]
    elif(act == 1):
        line = [sum(line), 0, 0, 0]
    else:
        a=1
    return line
def action(line, act, move):
    if move == 0 or move == 2:
        line = action_to_right(line, act)
    elif move == 1 or move == 3:
        line = action_to_left(line, act)
    return line
def pattern_detector(matrix, move):
    if move == 1 or move == 3:
        matrix = transpose(matrix)
    for i in range(4):
    #all same number
        if matrix[i].count(max(set(matrix[i]), key = matrix[i].count)) == 4:
            matrix[i] = action(matrix[i], 0, move)
    #3 zeros
        elif matrix[i].count(0) == 3:
            matrix[i] = action(matrix[i], 1, move)
        else:
            action(matrix[i], 2, move)


    return matrix
def main():
    # 0 - Left, 1 - Up, 2 - Right, 3- Down
    # left = up && right = down
    matrix, move = read_data()
    matrix = transpose(matrix, move)
    #matrix = pattern_detector(matrix, move)
    write_answer(matrix, move)

if __name__ == "__main__":
    main()
