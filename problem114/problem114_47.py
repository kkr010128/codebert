D = int(input())
clist = list(map(int, input().split()))
slist = [list(map(int, input().split())) for _ in range(D)]
tlist = [int(input()) for _ in range(D)]
zlist = []
dlist = [0] * 26
ans = 0
'''
print(sum(clist))
print('--------------')
print(slist[0][0])
print(slist[1][16])
print(clist[16])

print('--------------')
'''
for i in range(D):
  #print(slist[i],tlist[i]-1)
  zlist.append(clist[tlist[i]-1] * ((i+1) - dlist[tlist[i]-1]))
  dlist[tlist[i]-1] = i+1
  ans += slist[i][tlist[i]-1] - ((i+1) * sum(clist)) + sum(zlist)
  print(ans)