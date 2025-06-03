n=int(input())
a=[int(x) for x in input().split()]
mx=0
mae=a[0]
for i in a:
    if i<mae:
        mx=mx+mae-i
    else:
        mae=i
print(mx)