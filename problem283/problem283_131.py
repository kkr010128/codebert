N=int(input())
S=set()
for i in range(1,N):
    x=i
    y=N-i
    if x<y:
        S.add(x)
print(len(S))
