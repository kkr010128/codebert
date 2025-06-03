n=int(input())
a,b=map(str,input().split())
s=''
for i in range(n):
    s+=a[i]
    s+=b[i]
    
print(s)