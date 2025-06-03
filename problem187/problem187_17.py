import itertools

N,X,Y = list(map(int , input().split()))

combi = list(itertools.combinations(range(1,N+1),2))

ansList = [0 for _ in range(N)]

for i,j in combi:
    kyori = min(j-i, abs(j-Y) + abs(X-i) + 1)
    ansList[kyori] += 1
#    print(i,j,ansList)

for ans in ansList[1:]:
    print(ans)

