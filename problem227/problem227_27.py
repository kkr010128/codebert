n,k=map(int,input().split())
H = list(map(int, input().split()))

if n <= k:
  print('0')
  exit()

H.sort()
H.reverse()
print(sum(H)-sum(H[0:k]))
