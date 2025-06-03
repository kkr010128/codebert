from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
dic = defaultdict(int)
ans = sum(A)
for a in A:
    dic[a] += 1
Q = int(input())
for i in range(Q):
    b, c = map(int, input().split())
    ans -= dic[b] * b
    ans -= dic[c] * c
    dic[c] += dic[b]
    dic[b] = 0
    ans += dic[c] * c
    print(ans)
