# Kattis ABC
# by: Nathan Bellew

def SplitVariables(AB):
    AB = AB.split()
    A = int(AB[0])
    B = int(AB[1])
    C = int(AB[2])
    return A,B,C

def main():
    xyz = input()
    x,y,z = SplitVariables(xyz)
    yeet = [x,y,z]
    yeet.sort(reverse=True)
    abc = input()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    dic = {"C":yeet[0], "B":yeet[1], "A":yeet[2]}
    print(dic[a],  dic[b], dic[c])

if __name__ == "__main__":
    main()
