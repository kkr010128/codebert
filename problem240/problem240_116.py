N,M=map(int,input().split())
results = [False]*N
penalties = [0]*N
for _ in range(M):
    p,S=input().split()
    p = int(p)
    if S == 'AC':
        results[p-1] = True
    else:
        if not results[p-1]:
            penalties[p-1] += 1

points1 = 0
points2 = 0

for i in range(N):
    if results[i]:
        points1 += 1
        points2 += penalties[i]

print('{} {}'.format(points1,points2))
