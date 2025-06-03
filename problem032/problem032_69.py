n=int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))

for p in range(1,4):
    z=0
    for i in range(n):
        z+=(abs(x[i]-y[i]))**p
    print(f'{z**(1/p):.6f}')

c=[abs(x[i]-y[i]) for i in range(n)]
print(f'{max(c):.6f}')
