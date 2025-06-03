n = int(input())
S = set(map(int, input().split()))
q = int(input())
T = tuple(map(int, input().split()))

cnt = 0
for n in T:
    cnt += n in S

print(cnt)