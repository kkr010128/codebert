#ABC166-B
count=0
a=[]
n,k=map(int,input().split())
for i in range(k):
    d = int(input())
    a+=list((map(int, input().split())))
ans=(n-len(set(a)))
print(ans)