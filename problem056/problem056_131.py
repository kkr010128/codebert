n,m = list(map(int,input().split()))
A = [map(int,input().split()) for i in range(n)]
b = [int(input()) for i in range(m)]
for a in A:
    print(sum([x*y for (x,y) in zip(a,b)]))