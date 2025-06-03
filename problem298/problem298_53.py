number, req = map(int, input().split())

friends = list(map(int, input().split()))
allowed = 0
for i in friends:
  if i >=  req: allowed += 1
    
print(allowed)