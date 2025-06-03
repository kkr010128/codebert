n=int(input())
x=list(map(int, input().strip().split()))
X=0
for i in range(n):
    X+=x[i]
XX=0
for i in range(n):
    XX+=(x[i])**2
s=X//n
t=s+1
S=n*(s**2)-2*s*X+XX
T=n*(t**2)-2*t*X+XX
print(min(S,T))