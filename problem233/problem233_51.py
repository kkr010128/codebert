n=int(input())
p=list(map(int,input().split()))
sai = p[0]
answer = 1
for i in range(1,n):
    if p[i-1]<=sai:
        sai=p[i-1]
    if sai >= p[i]:
        answer = answer + 1
print(answer)