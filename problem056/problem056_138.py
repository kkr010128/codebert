m,n=map(int,input().split())
a=[]
b=[]
for _ in range(m):
    a.append(map(int, input().split()))
for _ in range(n):
    b.append(int(input()))
for ai in a:
    sum = 0
    for index, mi in enumerate(ai):
        sum += mi*b[index]
    print(sum)

