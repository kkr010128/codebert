A,B,M=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
m=[list(map(int,input().split())) for _ in range(M)]
min_a=min(a)
min_b=min(b)

min_cost=min_a+min_b
for _m in m:
  cost=a[_m[0]-1]+b[_m[1]-1]-_m[2]
  min_cost=min(min_cost,cost)
print(min_cost)




