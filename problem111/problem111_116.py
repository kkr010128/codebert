n=int(input())
a=sorted(list(map(int,input().split())))
c=0
for i in range(n-1):
    c+=a[-1-(i+1)//2]
print(c)
