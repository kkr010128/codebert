import collections
s = list(input())
n = len(s)
mod = [0]*(n+1)
pow10 = 1
for i in range(n):
    mod[i+1] = (mod[i] + int(s[-1-i])*pow10)%2019
    pow10 = pow10*10%2019
d = collections.Counter(mod)
ans = 0
for i in d.values():
    ans += i*(i-1)//2
print(ans)
