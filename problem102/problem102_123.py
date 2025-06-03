n, k = map(int, input().split())
lis = list(map(int, input().split()))
lis_score = []


for i in range(n):

  if i >= k:
    lis_edge_right = lis[i]
    lis_edge_left = lis[i-k]
    
    if lis_edge_right > lis_edge_left:
      print("Yes")
    else:
      print("No")

