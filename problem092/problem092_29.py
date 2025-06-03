a,k,d = map(int, input().split())

if a < 0:
    x = -a
else:
    x = a

y = x % d
l = x // d
m = k - l

if m < 0:
    ans = x - (k * d)
elif m % 2 ==0:
    ans = y
else :
    ans = y - d

print(abs(ans))