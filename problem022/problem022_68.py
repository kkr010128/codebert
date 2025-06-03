n = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]
cnt = 0
for T in T:
    if T in S:
        cnt += 1
print(cnt) 