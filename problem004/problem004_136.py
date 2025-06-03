n=int(input())
for i in range(n):
    p=list(map(int,input().split(" ")))
    p.sort()
    if pow(p[0],2) + pow(p[1],2) == pow(p[2],2):
        print('YES')
    else:
        print('NO')
