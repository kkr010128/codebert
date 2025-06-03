s=input()
n=len(s)
a=[0]*(n+1)
for i in range(n):
    if s[i]=="<":
        a[i+1]=a[i]+1
for i in reversed(range(n)):
    if s[i]==">":
        a[i]=max(a[i+1]+1,a[i])
print(sum(a)) 