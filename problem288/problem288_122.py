N = int(input())
dmin = N+N
for i in range(1,int(N**0.5)+1):
    if N%i==0:
        dmin = min(dmin,i+N//i-2)
print(dmin)