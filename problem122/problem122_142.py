n = int(input())
lst = [0]*(10**5)

l = list(map(int,input().split()))
total = sum(l)  
for x in l:
  lst[x-1] += 1

  
m = int(input())  
for i in range(m):
  x,y = map(int,input().split())
  lst[y-1] += lst[x-1]
  total += (y-x) * lst[x-1]
  lst[x-1] = 0  
  print(total)

