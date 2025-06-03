a,b,c,d = map(int,input().split())
val = [None]*4
val = [a*c,a*d,b*c,b*d]

top = a*c

for i in range(1,4):
    if top < val[i]:
        top = val[i]

print(top)