n, k = map(int, input().split())
card = {x : i for x, i in zip (("s", "p", "r") , map(int, input().split()))}
t = input()
ans = [0]*k

for i in range(k):
    chk = 0
    for j in range(i, n, k):
        if j < k:
            tmp, chk = card[t[j]], 1
        elif t[j] != t[j-k]:
            tmp, chk = card[t[j]], 1
        elif chk == 0 and t[j] == t[j-k]:
            tmp, chk = card[t[j]], 1
        else:
            tmp, chk = 0, 0
        ans[i] += tmp
print(sum(ans))

