n,m = map(int,input().split())
rc = [list(map(int,input().split())) for i in range(n)]
vector = [int(input()) for i in range(m)]
[print(sum([j*k for j,k in zip(rc[i],vector)])) for i in range(n)]