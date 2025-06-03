x = list(map(int, input().split()))  # n個の数字がリストに格納される

for i in range(5):
  if x[i] is 0:
    print(i+1)