a,b,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
xyc = [list(map(int,input().split())) for nesya in range(m)]
cheap = min(a)+min(b)
for hoge in xyc:
  ch = a[hoge[0]-1]+b[hoge[1]-1]-hoge[2]
  cheap = min(ch,cheap)
print(cheap)