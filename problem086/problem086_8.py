n,x,t = map(int,(input().split()))
i = 1
while 1:
    if n > x*i:
        i += 1
    if n <= x*i:
        break
print(t*i)