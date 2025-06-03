a,b,m = map(int,input().split())
a_li = list(map(int,input().split()))
b_li = list(map(int,input().split()))
cost = min(a_li) + min(b_li)
for i in range(m):
  x,y,c = map(int,input().split())
  price = a_li[x-1] + b_li[y-1] - c
  if price < cost:
    cost = price
print(cost)
