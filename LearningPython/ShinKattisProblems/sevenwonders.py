def main():
    l = input()
    line = list(l)
    mini =[]
    mini.append(line.count("T"))
    mini.append(line.count("C"))
    mini.append(line.count("G"))
    print(min(mini)*7 + mini[0]**2+mini[1]**2+mini[2]**2)
if __name__ == "__main__":
    main()
