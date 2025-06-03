N, M = map(int, input().split())
A = list(map(int,input().split()))
A.sort()
total=sum(A)
i=0
flg="Yes"
while i < M:
    if A.pop() < total/(4*M):
        flg="No"
        break
    i += 1
print(flg)