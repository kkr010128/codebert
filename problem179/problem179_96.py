
N, M = map(int, input().split())
A = list(map(int, input().split()))


line = sum(A)/(4*M)
cnt = 0
for a in A:
    if a >= line:
        cnt += 1
if cnt >= M:
    print("Yes")
else:
    print("No")
