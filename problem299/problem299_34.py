n = int(input())
al = list(map(int,input().split()))

lst = [[] for _ in range(n)]
for i in range(1,n+1):
  lst[al[i-1]-1] = i
print(*lst)
  
