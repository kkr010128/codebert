from itertools import combinations
N = int(input())
P = [tuple(map(int,input().split())) for _ in range(N)]

total = sum(((x0-x1)**2+(y0-y1)**2)**(1/2) for (x0,y0),(x1,y1) in combinations(P,2))

print(2*total/N)
