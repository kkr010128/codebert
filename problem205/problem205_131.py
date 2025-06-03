from collections import Counter

N, P = map(int, input().split())
S = input()

def check(n):
    ans = 0
    for i in range(1, N+1):
        v = int(S[-i])
        if v%n==0:
            ans += N-(i-1)
    return ans

ans = 0
if P==2:
    ans = check(2)
elif P==5:
    ans = check(5)
else:
    ac = [0]*(N+1)
    for i in range(1, N+1):
        ac[i] = (ac[i-1]+int(S[-i])*pow(10, i-1, P))%P
    c = Counter(ac)
    for i in c.values():
        ans += i*(i-1)//2

print(ans)