n = int(raw_input())
S = map(int,raw_input().split())
q = int(raw_input())
T = map(int,raw_input().split())

c = 0
for t in T:
    for s in S:
        if(t == s):
            c+=1
            break
print c