n = int(raw_input())
S = map(int,raw_input().split())
q = int(raw_input())
T = map(int,raw_input().split())

C = 0
for i in T:
    for j in S:
        if i == j:
            C += 1
            break
print C