A,B,C = map(int,input().split())

if A == B:
    if A != C:
        print("Yes")
    else:
        print("No")
else:
    if B == C or A == C:
        print("Yes")
    else:
        print("No")