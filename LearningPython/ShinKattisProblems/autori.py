name = input()
namelist =list(name)

string = ""
for i in namelist:
    if i.isupper():
        string += i
print(string)
