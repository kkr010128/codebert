
S=int(input())
A=list(input().split())

T=int(input())
B=list(input().split())

n=0

for i in B:
    if i in A:
        n=n+1

print(n)

