
def main():
    line = input()
    line=list(line)
    ans = []
    for i in range(len(line)):
        if line[i] == '<':
            ans.pop(-1)
        else:
            ans.append(line[i])
    print("".join(ans))

if __name__=="__main__":
    main()
