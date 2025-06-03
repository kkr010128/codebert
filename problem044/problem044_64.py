a,b,c = map(int, input().split())
p = 0
for j in range(a,b + 1):
    if c%j==0:
        p = p+1
print(p)

