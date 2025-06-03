n=int(input())
a,b=map(str, input().split()) 
l = []

for i in range(n):
    l.append(a[i])
    l.append(b[i])

print(''.join(l))