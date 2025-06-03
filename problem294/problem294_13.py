import bisect
 
N = int(input())
Ls = list(map(int, input().split(" ")))
Ls.sort()
 
ans = 0
 
for i in range(0,N-2):
  for j in range(i+1,N-1):
    k = bisect.bisect_left(Ls,Ls[i]+Ls[j])
    ans += k - (j + 1)
       
print(ans)