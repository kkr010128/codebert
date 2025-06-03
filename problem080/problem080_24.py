N = int(input())
z = []
w = []
for i in range(N):
    x,y = map(int,input().split())
    z.append(x+y)
    w.append(x-y)

z_max = max(z)
z_min = min(z)
w_max = max(w)
w_min = min(w)

print(max(z_max-z_min,w_max-w_min))