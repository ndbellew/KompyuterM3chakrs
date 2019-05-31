
def main():
    index,ans = 1,0
    iterations = int(input())
    l = []
    for i in range(iterations):
        C = int(input())
        l.append(C)
    l = sorted(l, reverse=True)
    for i in l:
        if i < index:
            ans = index-1
        else:
            index+=1
    if ans == 0:
        print(index-1)
    else:
        print(ans)


if __name__ == "__main__":
	main()
