n=int(input())
n-=1
a='abcdefghijklmnopqrstuvwxyz'
a=list(a)
ans=''
for i in range(1,20):
    if n<26**i:
        for j in range(i):
            ans+=a[n%26]
            n//=26
        break
    else:
        n-=26**i
print(ans[::-1])
    

