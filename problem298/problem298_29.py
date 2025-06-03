N,K=map(int,input().split())
H=list(map(int,input().split()))

S=0
for h in H:
    S+=h>=K
print(S)