import math, sys

N=int(input())
S=input()
R_count=0
if "R" not in S:
    print(0)
    sys.exit()
if "W" not in S:
    print(0)
    sys.exit()
if "R" not in S[S.index("W"):]:
    print(0)
    sys.exit()
for i in range(N):
    if S[i]=="R":
        R_count+=1

S=S[:R_count]
ans=S.count("W")
print(ans)