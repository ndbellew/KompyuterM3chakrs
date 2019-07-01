def sum_counter(sum):
    total = 0
    while sum > 0:
        digit = sum%10
        total += digit
        sum = sum//10
    return total
def main():
    answer = []
    while True:
        num = int(input())
        sum1 = sum_counter(num)
        sum2 = 0
        i = 10
        if num != 0:
            while sum1 != sum2:
                i += 1
                sum2 = sum_counter(num*i)
            answer.append(i)
        else:
            break
    for i in range(len(answer)):
        print(answer[i])
if __name__ == "__main__":
    main()
