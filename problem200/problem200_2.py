a,b,m = map(int,input().split())
a_list = [int(x.strip()) for x in input().split()]
b_list = [int(x.strip()) for x in input().split()]
ans = min(a_list)+min(b_list)
for i in range(m):
  ai,bi,ci = map(int,input().split())
  ch = a_list[ai-1]+b_list[bi-1]-ci
  if ch < ans:
    ans = ch
print(ans)