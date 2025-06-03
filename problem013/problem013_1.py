N = input()
a = [input() for i in range(N)]

def smax(N,a):
  smin = a[0]
  smax = -10**9
  for j in range(1,N):
   smax = max(smax,a[j]-smin)
   smin = min(smin,a[j])
  return smax

print smax(N,a)