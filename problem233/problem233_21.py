n=int(input(''))
p=list(map(int,input('').split(' ')))
s=1
mi=p[0]
for a in range(n-1):
    if p[a+1]<=mi:
        s=s+1
        mi=p[a+1]

print(s)