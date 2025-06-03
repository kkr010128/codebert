k=int(input())

def dfs(keta, val):
  lunlun.append(val)

  if keta==10:
    return

  for i in range(-1,2):
    add=(val%10)+i
    if 0<=add<=9:
      dfs(keta+1, val*10+add)

lunlun=[]
for i in range(1,10):
  dfs(1, i)

lunlun.sort()
print(lunlun[k-1])