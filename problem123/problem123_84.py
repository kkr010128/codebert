n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    s=s^l[i]
k=s
y=0
for i in range(n):
   y=k^l[i]
   print(y,end=" ")
