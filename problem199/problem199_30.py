import sys
S = list(input())
if (len(S) % 2 == 1):
    print("No")
    sys.exit()
pre = S.pop(0)
for s in S:
    if(pre == "h"):
        if(s != "i"):
            print("No")
            sys.exit()
    elif(pre != "i"):
        print("No")
        sys.exit()
    pre = s
print("Yes")



