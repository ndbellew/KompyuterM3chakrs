#! /bin/python3
import string


alphalower = list(string.ascii_lowercase)
alphaupper = list(string.ascii_uppercase)
symbolList = list("~!@#$%^&*()\"\'-+=}][{|/>.<,\\1234567890")

def main():
    whitespace, upper, lower, symbol = 0.0,0.0,0.0,0.0
    total,ws,upp,lw,sym = 0.0,0.0,0.0,0.0,0.0
    phrase = list(input())
    for i in phrase:
        total+=1.0
        if i in symbolList:
            symbol +=1.0
        elif i in alphalower:
            lower+=1.0
        elif i in alphaupper:
            upper+=1.0
        elif i =="_":
            whitespace+=1.0
        else:
            pass
    ws = float(whitespace)/total
    upp = float(upper)/total
    lw = float(lower)/total
    sym = float(symbol)/total

    print("%.6f"%ws)
    print("%.6f"%lw)
    print("%.6f"%upp)
    print("%.6f"%sym)

if __name__ == "__main__":
    main()
