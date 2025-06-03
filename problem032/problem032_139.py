n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

for i in range(1,4):
    cnt=0
    for j in range(n):
        cnt+=abs(A[j]-B[j])**i
    print(cnt**(1/i))
cnt=0
for j in range(n):
    cnt=max(cnt,abs(A[j]-B[j]))
print(cnt)
