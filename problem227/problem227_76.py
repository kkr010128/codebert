N,K = map(int, input().split())
H = list(map(int, input().split()))

H_sort = sorted(H)

#print (H)

if K > N:
  print(0)
else:
  ans = sum(H_sort[0:N-K])
  print(ans)