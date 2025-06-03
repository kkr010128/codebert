K = int(input())

def f(n, k, a):
    if k == n:
        return 1
    res = 0
    res += f(n, k+1, a)
    if a > 0:
        res += f(n, k+1, a-1)
    if a < 9:
        res += f(n, k+1, a+1)
    return res


cnt = 0
for n in range(1, 12):
    c2 = 0
    for a in range(1, 10):
        c2 += f(n, 1, a)
        if cnt+c2 >= K:
            num = n
            ini = a
            cnt += c2-f(n, 1, a)
            c2 = -1
            break
    if c2 < 0:
        break
    cnt += c2

ans = [ini]
for k in range(2, num+1):
    for a in range(max(0, ans[-1]-1), min(10, ans[-1]+2)):
        cnt += f(num, k, a)
        if cnt >= K:
            ans.append(a)
            cnt -= f(num, k, a)
            break

for i in range(len(ans)):
    ans[i] = str(ans[i])
print("".join(ans))