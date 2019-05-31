import math

def main():
    h, a = input().split()
    h = float(h)
    a = float(a)
    b = h * math.tan((90-a)*(float(math.pi/180)))
    l = h**2 + b**2
    print(int(math.ceil(math.sqrt(l))))


if __name__ == "__main__":
    main()
