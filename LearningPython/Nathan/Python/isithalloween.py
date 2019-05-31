def main():
    X = input().split()
    if (X[0]=="OCT" and X[1]=="31") or (X[0]=="DEC" and X[1]=="25"):
        print("yup")
    else:
        print("nope")
if __name__=="__main__":
    main()
