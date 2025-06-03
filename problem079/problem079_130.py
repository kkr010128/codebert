s = int(input())
a = [0] * (s+1)

if s == 1:
    print(0)
else:
    a[0]=1
    a[1]=0
    a[2]=0
    mod = 10**9+7
    for i in range(3,s+1):
        a[i] = a[i-1]+a[i-3]
    print(int(a[s] % mod))