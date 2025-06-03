N = int(input())
A = list(map(int, input().split()))

MAX = 0
A_map = {}
for i in range(N):
    num = A[i]
    A_map[num] = A_map.get(num,0) + 1
    MAX = max(MAX, A_map[num])

if MAX>=2:
    print('NO')
else:
    print('YES')