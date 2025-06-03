x = list(map(int,input().split()))
x.reverse()
a = x.index(0)
if a == 4:
    print(x[a-1]-1)
else:
    print(x[a+1]+1)

