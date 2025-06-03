# 解説

n,k,c = map(int, input().split())
s = input()

l = [0 for i in range(n)]
r = [-1 for i in range(n)]

a = 1
b = -1
for i in range(n):
    if s[i]=='o' and b<i:
        l[i]=a
        a+=1
        b=i+c
        if a>k:
            break

a = k
b = n
for i in range(n):
    if s[-i-1]=='o' and b>n-i-1:
        r[-i-1]=a
        a-=1
        b=n-i-1-c
        if a<1:
            break

for i in range(n):
    if l[i]==r[i]:
        print(i+1)
