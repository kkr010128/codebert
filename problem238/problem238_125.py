n, k, s = map(int, input().split())

la = list()

if s == 1:
    l = [1] * k + [2] * (n-k)

elif s == 10**9:
    l = [s] * k + [1] * (n-k)

else:
    l = [s] * k + [s+1] * (n-k)

l = [str(i) for i in l]
print(" ".join(l))