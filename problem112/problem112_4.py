n, k = map(int, input().split())

a = list(map(int, input().split()))
a_pos = sorted([i for i in a if i >= 0])
a_neg = sorted([i for i in a if i < 0], reverse=True)

mod = 10 ** 9 + 7
ans = 1

if len(a_pos) == 0 and k % 2:
    for i in a_neg[:k]:
        ans = ans * i % mod
    print(ans)
    exit()

while k > 0:
    if k == 1 or len(a_neg) <= 1:
        if len(a_pos) == 0:
            ans *= a_neg.pop()
        elif len(a_pos) > 0:
            ans *= a_pos.pop()
        k -= 1
    elif len(a_pos) <= 1:
        ans *= a_neg.pop() * a_neg.pop()
        k -= 2
    
    elif a_pos[-1] * a_pos[-2] > a_neg[-1] * a_neg[-2]:
        ans *= a_pos.pop()
        k -= 1
    elif a_pos[0] * a_pos[1] <= a_neg[-1] * a_neg[-2]:
        ans *= a_neg.pop() * a_neg.pop()
        k -= 2
    ans %= mod

print(ans)