n, k = map(int, input().split())
l = list(map(int, input().split()))
start = k
c = 0
for i in range(n-k):
    if l[start]>l[c]:
      print("Yes")
    else:
      print("No")
    start+=1
    c+=1