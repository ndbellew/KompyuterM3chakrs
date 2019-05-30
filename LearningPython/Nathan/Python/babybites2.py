num_of_elements = int(input())
elements = input().split()
success = True
for i in range(0,num_of_elements-1,1):
    if elements[i] == "mumble":
        pass
    elif int(elements[i]) == i+1:
        pass
    else:
        success = False
if success:
     print("makes sense")
else:
    print("something is fishy")
