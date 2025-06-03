n, k, c = map(int, input().split())
s = input()

l = [0] * k
r = [0] * k
l_idx = 0
r_idx = k - 1
l_cnt = r_cnt = 0
for i in range(n):
    if s[i] == "o" and (l_cnt >= c or l_idx == 0) and l_idx < k:
        l[l_idx] = i
        l_cnt = -1
        l_idx += 1
    if s[n-i-1] == "o" and (r_cnt >= c or r_idx == k - 1) and r_idx >= 0:
        r[r_idx] = n - i - 1
        r_cnt = -1
        r_idx -= 1
    l_cnt += 1
    r_cnt += 1

for i in range(k):
    if l[i] == r[i]:
        print(l[i] + 1)