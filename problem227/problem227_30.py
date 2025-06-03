n,k = map(int,input().split())

h = [0 for _ in range(n)]
h = [int(s) for s in input().split()]

h.sort()
#print(h)
if(n-k <= 0):
  ans = 0
else:
  h_new = h[:n-k]
  #print(h_new)
  ans = sum(h_new)

print(ans)