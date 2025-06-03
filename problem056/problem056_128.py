n,m=list(map(int,input().split()))
mA=[list(map(int,input().split())) for i in range(n)]
mB=[int(input())  for j in range(m)]

for ma in mA:
    print(sum([a*b for a, b in zip(ma,mB)]))