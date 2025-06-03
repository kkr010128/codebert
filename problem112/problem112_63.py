N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

neg_a = sorted([a for a in A if a < 0], reverse=True)
pos_a = sorted([a for a in A if a >= 0])
ans = 1

if len(pos_a) == 0 and K % 2 == 1:
    for a in neg_a[:K]:
        ans = ans * a % MOD
    print(ans)
    exit()

while K > 0:
    if K == 1 or len(neg_a) <= 1:
        if len(pos_a) == 0:
            ans *= neg_a.pop()
        elif len(pos_a) > 0:
            ans *= pos_a.pop()
        K -= 1
    elif len(pos_a) <= 1:
        ans *= neg_a.pop() * neg_a.pop()
        K -= 2
    elif pos_a[-1] * pos_a[-2] > neg_a[-1] * neg_a[-2]:
        ans *= pos_a.pop()
        K -= 1
    else:
        ans *= neg_a.pop() * neg_a.pop()
        K -= 2
    ans %= MOD

print(ans)
