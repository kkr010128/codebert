n = int(input())
a = map(int,raw_input().split())
p = int(input())
m = map(int,raw_input().split())
def goukei(i,m):
  if m ==0:
    return True
  if i >= n or m > sum(a):
    return False
  r = goukei(i + 1, m) or goukei(i + 1, m - a[i])
  return r
 
for u in range(0,p):

  if goukei(0, m[u]):
    print "yes"
  else:
    print "no"