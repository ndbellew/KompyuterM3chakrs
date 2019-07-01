def remove_zeros(num):
    nums = list(num)
    indexes = (list(reversed(range(len(nums)))))
    for i in indexes:
        if nums[i] == '0':
            del nums[-1]
        else:
            break
    return "".join(nums)
def main():
    n = int(input())
    list = []
    for i in range(n):
        x, y = input().split()
        x = int(x)
        y = float(y)
        list.append([x,y])
    area = 0
    for i in range(n-1):
        area += (list[i+1][0]-list[i][0])*((list[i+1][1]+list[i][1])/2)
    answer = 0

    if int(area/1000) == float(area/1000):
        print(int(area/1000))
    else:
        answer = str(round((float(area/1000)),10))
        print(remove_zeros(answer))
if __name__ == "__main__":
  main()
