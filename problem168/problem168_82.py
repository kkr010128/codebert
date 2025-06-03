N, M = map(int, input().split())
C = list(map(int, input().split()))
hw = 0
for i in range(M):
    hw += C[i]

d = N - hw
if d >= 0:
    print(d)
else:
    print('-1')