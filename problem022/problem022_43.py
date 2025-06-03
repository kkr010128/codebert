n = input()
S = map(int,raw_input().split())
q = input()
T = map(int,raw_input().split())
ans = 0
for t in T:
    if t in S:
        ans+=1
print ans