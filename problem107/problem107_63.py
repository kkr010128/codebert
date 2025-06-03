def cin():
    return input().split()
def qpow(a,b,p):
    if p == 1 or p == 0:
        return 0
    a = (a%p+p)%p
    ans = 1
    while b!=0:
        if (b&1) != 0:
            ans = (ans * a) % p
        b >>= 1
        a = a * a  % p
    return ans

def f(n):
    if n == 0:
        return 0
    return f(n % bin(n).count("1")) + 1

n = int(input())
x = list(input())
x = x[::-1]
cnt = 0;l = len(x)
r1 = 0;r2 = 0
for i in x:
    if i == '1':
        cnt += 1
i = 0
while i < l:
    if x[i] == '1':
        r1 += qpow(2,i,cnt+1)
        r2 += qpow(2,i,cnt-1)
    i += 1
i = 0
a = []
while i < l:
    if x[i] == '0':
        t = f((r1+qpow(2,i,cnt+1))%(cnt+1))+ 1
    else:
        if cnt-1 !=  0:
            t = f((r2-qpow(2,i,cnt-1)+(cnt-1))%(cnt-1)) + 1
        else:
            t = 0
    i += 1
    a.append(t)
a = a[::-1]
for i in a:
    print(i)


