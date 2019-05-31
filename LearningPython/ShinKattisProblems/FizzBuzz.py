def main():
    a, b, n = input().split()

    a = int(a)
    b = int(b)
    n = int(n)

    list = ["Fizz", "Buzz", "FizzBuzz"]

    for i in range(1, n+1):
        if i%a == 0 and i%b == 0:
            print(list[2])
        elif i%a == 0:
            print(list[0])
        elif i%b == 0:
            print(list[1])
        else:
            print(i)

if __name__ == "__main__":
    main()
