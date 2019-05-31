x=int(input("Enter x-coordinate: "))
y=int(input("Enter y-coordinate: "))

if y>=0 and x>=0:
    print("1")
elif y>=0 and x<0:
    print("2")
elif y<0 and x<0:
    print("3")
else:
    print("4")
