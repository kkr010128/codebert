n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10 ** 9 + 7

if max(a) < 0:
    a.sort()
    ans = 1
    if k % 2 == 0:
        for e in a[:k]:
            ans *= e
            ans %= mod
    else:
        for e in a[-k:]:
            ans *= e
            ans %= mod

    print(ans)

elif k == n:
    ans = 1
    for e in a:
        ans *= e
        ans %= mod

    print(ans)

else:
    neg = []
    pos = []
    for e in a:
        if e < 0:
            neg.append(e)
        else:
            pos.append(e)

    neg.sort()
    pos.sort(reverse=True)

    ans = 1
    if k % 2:
        ans *= pos.pop(0)
        k -= 1

    nums = [e1 * e2 for e1, e2 in zip(neg[::2], neg[1::2])]
    nums += [e1 * e2 for e1, e2 in zip(pos[::2], pos[1::2])]

    nums.sort(reverse=True)
    for e in nums[:k//2]:
        ans *= e
        ans %= mod

    print(ans)
