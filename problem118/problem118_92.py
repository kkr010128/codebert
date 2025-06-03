n = int(input())

s = int(n*(n+1)/2)

for l in range(2,n+1):
    i = 1
    while l*i <= n:
        s += l*i
        i += 1
print(s)