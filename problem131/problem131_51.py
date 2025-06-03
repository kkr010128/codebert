a,v=map(int,input().split())
b,w=map(int,input().split())
t=int(input())
if v<w:
  print("NO")
  exit()
diff=abs(a-b)
for _ in range(t):
  diff=diff-v+w
  if diff<=0:
    print("YES")
    exit()
print("NO")