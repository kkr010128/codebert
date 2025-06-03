N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
d = 0
for i in range(N-1):
    for j in range(i+1,N):
        d += ((a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2)**(1/2)
print(2*d/N)