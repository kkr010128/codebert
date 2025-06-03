l = list(map(int,input().split()))
mx = float('-inf')

for i in range(2):
  for j in range(2,4):
    mx = max(mx,l[i]*l[j])
print(mx)