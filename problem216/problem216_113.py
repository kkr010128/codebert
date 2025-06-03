A, B, C = map(int, input().split())

if (A == B and B == C) or (A != B and B != C and A != C):
    print("No")
else:
    print("Yes")
