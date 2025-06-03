N=int(input())
A=list(map(int,input().split()))

count=0

for i,a in enumerate(A):
    n=i+1
    if n%2==1 and a%2==1:
        count+=1

print(count)