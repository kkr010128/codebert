n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
ret = 0
for i in range(k):
    last = 'x'
    for c in t[i::k]:
        if last != c:
            ret += p if c == 'r' else r if c == 's' else s
            last = c
        else:
            last = 'x'
print(ret)

