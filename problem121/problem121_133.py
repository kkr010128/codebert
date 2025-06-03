N = int(input())
L = list("abcdefghijklmnopqrstuvwxyz")
a = 1
while N > 26**a:
    N = N - 26**a
    a += 1
 
pre = []
for i in reversed(range(1,a)):
    r = (N-1) // 26**i
    pre.append(r)
    N = int(N%(26**i))
 
ans = ''
for i in pre:
    ans += L[i]
print(ans+L[N-1])