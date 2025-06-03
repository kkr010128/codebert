n = int(input())
S = map(int,raw_input().split())
q = int(input())
T = map(int,raw_input().split())
count = 0
for v in T:
    for i in range(n):
        if S[i] == v:
            count += 1
            break
print count