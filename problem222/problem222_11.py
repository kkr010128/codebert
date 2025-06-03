import collections 
n = int(input())
a = map(int,input().split())
c = collections.Counter(a)
c = c.values()
for i in c:
  if i!=1:
    print("NO")
    exit()
print("YES")