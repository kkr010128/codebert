a,b,c = [int(i) for i in input().split()]
i=0
for num in range(a,b+1,1):
    if c % num == 0:
        i = i+1
    else:
        pass
print(i)
