s = input()
t = input()
slist = list(s)
tlist = list(t)
count = 0
if len(slist)+1 == len(tlist):
    for i in range(len(slist)):
        if slist[i] == tlist[i]:
            count += 1
            if count ==len(slist):
                print("Yes")
        else:
            print("No")
            break
else:
    print("No")