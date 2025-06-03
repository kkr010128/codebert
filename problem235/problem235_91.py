from collections import defaultdict

ps = []
for i in range(2, 1000):
    is_p = True
    for j in range(2, i):
        if i % j == 0:
            is_p = False
            break
    if is_p:
        ps.append(i)

def factorization(n):
    arr = defaultdict(int)
    temp = n
    for i in ps:
        if i > int(-(-n**0.5//1))+1:
            break
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt
    if temp!=1:
        arr[temp] = 1
    if arr==[]:
        arr[n] = 1
    return arr


aa = defaultdict(int)

n = int(input())
a = list(map(int, input().split()))

fs = [[]] * 1000001
for i in a:
    if not fs[i]:
        fs[i] = factorization(i)

for i in a:
    for k, v in fs[i].items():
        aa[k] = max(aa[k], v)


mod = 10 ** 9 + 7
t = 1
for k, v in aa.items():
    t = (t * (k ** v)) % mod
ans = 0
for i in a:
    ans += t * pow(i, mod - 2, mod)
    ans %= mod
print(ans)
