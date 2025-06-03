a,b,c,k = map(int,input().split())
#l = [1 for i in range(a)] + [0 for i in range(b)] + [-1 for i in range(c)]
#ans = sum(l[:k])
if k <= a:
    ans = k
elif (a < k) & (k <= a + b):
    ans = a
elif (a + b < k) & (k <= a + b + c):
    ans = a - (k - (a + b))

print(ans)