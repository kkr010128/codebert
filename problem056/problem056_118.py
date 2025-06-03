n, m = map(int, input().split())
mat = [map(int,input().split()) for i in range(n)]
vec = [int(input()) for i in range(m)]
for row in mat:
    print(sum([a*b for (a,b) in zip(row, vec)]))