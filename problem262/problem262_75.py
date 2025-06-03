N=int(input())
Ins=[[] for _ in range(N)]
ans=0

#0-indexedにしておく
for i in range(N):
  A=int(input())
  for _ in range(A):
    x,y=map(int,input().split())
    Ins[i].append((x-1,y))

for i in range(2**N):
  flag=1
  honest=[]
  unkind=[]
  for j in range(N):
    if (i>>j)&1:
      honest.append(j)
    else:
      unkind.append(j)
      #ここまでは想定の組み合わせを作る作業
  for k in honest:
    #honestな人の証言を見ていく
    for l in Ins[k]:
      if l[1]==1 and l[0] in unkind:
        flag=0
        break
        #honestな人がある人物をhonestと答えたのにも関わらず
        #その人がunkindに入るような組み合わせは駄目...ケース1
      elif l[1]==0 and l[0] in honest:
        flag=0
        break
        #honestな人がある人物をunkindと答えたのにも関わらず
        #その人がhonestに入るような組み合わせは駄目...ケース2
  if flag==1:
    ans=max(ans,len(honest))
    #ケース1にもケース2にも該当しない場合
    #現在のhonestの人数をansと比較して大きい方を採用
print(ans)