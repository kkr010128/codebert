N = int(input())

a = [int(i) for i in input().split()]

cnt = 0
for i,v in enumerate(a,1):
  if i%2 != 0 and v%2 != 0:
    cnt += 1
    
print(cnt)