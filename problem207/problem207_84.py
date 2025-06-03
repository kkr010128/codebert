a = input("").split(" ")
a = [int(aa) for aa in a]
b = input("").split(" ")
b = [int(ab) for ab in b]
c = input("").split(" ")
c = [int(ac) for ac in c]
n = int(input(""))
hav = a + b + c
val = []
for d in range(n):
    temp = int(input(""))
    val.append(temp)
tf = [0,0,0,0,0,0,0,0,0]
i = 0
for e in hav:
    if (e in val) == True:
        tf[i] = 1
    i += 1
tr = [1,1,1]
if tf[0:3] == tr:
    print("Yes")
elif tf[3:6] == tr:
    print("Yes")
elif tf[6:9] == tr:
    print("Yes")
elif (tf[0]+tf[3]+tf[6]) == 3:
    print("Yes")
elif (tf[1]+tf[4]+tf[7]) == 3:
    print("Yes")
elif (tf[2]+tf[5]+tf[8]) == 3:
    print("Yes")
elif (tf[0]+tf[4]+tf[8]) == 3:
    print("Yes")
elif (tf[2]+tf[4]+tf[6]) == 3:
    print("Yes")
else:
    print("No") 