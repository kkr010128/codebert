N=int(input())
A=list(map(int,input().split()))
p=round(sum(A)/N)
print(sum(map(lambda x: (x-p)**2, A)))