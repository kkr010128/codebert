a,b,c,k = map(int,input().split())
s = 0

if k <= a:
    s = k
elif k <= a + b:
    s = a
else:
    s = a - (k - a - b)

print(s)