def main():


    count_b = 0
    count_w = 0
    line = input()
    for i in range(0, len(line)):
        if line[i] == 'W':
            count_w += 1
        if line[i] == 'B':
            count_b += 1
    if count_b == count_w:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
