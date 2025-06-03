D,T,S = (int(x) for x in input().split())

disable = D - T*S

if disable>0:
    print("No")
else:
    print("Yes")