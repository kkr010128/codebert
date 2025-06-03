K,N = map(int,input().split())
l1 = list(map(int,input().split()))
l2 = [l1[i]-l1[i-1] for i in range(len(l1))]
l2[0] = l1[0] + K - l1[-1] 
l2.sort()
ans = 0
for i in range(N-1):
  ans += l2[i]
print(ans)