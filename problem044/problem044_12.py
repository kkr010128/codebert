[a,b,c] = map(int,input().split())
n = 0
i = a
while i <= b:
    if c % i == 0:
        n += 1
    i += 1    
print(n) 