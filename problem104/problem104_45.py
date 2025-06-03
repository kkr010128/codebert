a = list(map(int, input().rstrip().split()))
resto=a[0]%a[-1]
if resto >0:
    o = a[0]+a[-1]- resto
else:
    o= a[0]
print((a[1]-o)//a[-1]+1)
