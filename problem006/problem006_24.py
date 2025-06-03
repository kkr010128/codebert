S=100000
n=int(input())
for i in range(n):
    S*=1.05
    S=int(S)
    if S%1000==0:
        S=S
    else:
        S=S+1000
    S=S//1000
    S=S*1000
print(S)
