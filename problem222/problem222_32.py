N=int(input())
ListIN = list(map(int, input().split()))
s_l=set(ListIN)
if len(ListIN) == len(s_l):
  print("YES")
else:
  print("NO")