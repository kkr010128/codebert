n=int(input())
x = [int(x) for x in input().split()]

heikin=(sum(x)/n)

if abs(int(heikin)-heikin)<abs(int(heikin+1)-heikin):
    kaisai=int(heikin)
else:
    kaisai=int(heikin+1)

ans=0

for i in x:
    ans+=(i-kaisai)**2

print(ans)