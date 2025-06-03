n = int(input())
p = [1,1]

if n <= 1:
    print (1)
    exit (0)

for i in range(2,n+1):
    p.append(p[i-2] + p[i-1])

print (p[n])
