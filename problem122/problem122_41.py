from collections import Counter

n = int(input())
a = list(map(int, input().split()))
q = int(input())
b = [0] * q
c = [0] * q
for i in range(q):
    b[i], c[i] = map(int, input().split())

ans = sum(a)
a_c = Counter(a)

for i in range(q):
    b_num = a_c[b[i]]
    ans += (c[i] - b[i]) * b_num
    a_c[c[i]] += b_num
    a_c[b[i]] = 0
    print(ans)
