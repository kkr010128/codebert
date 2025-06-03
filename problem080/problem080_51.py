n=int(input())
z_max,z_min=-10**10,10**10
w_max,w_min=-10**10,10**10
for i in range(n):
    a,b=map(int,input().split())
    z=a+b
    w=a-b
    z_max=max(z_max,z)
    z_min=min(z_min,z)
    w_max=max(w_max,w)
    w_min=min(w_min,w)
print(max(z_max-z_min,w_max-w_min))