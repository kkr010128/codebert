H,W,K = map(int, input().split())

def cv(S,cn,pr):
  SS=S
  ans = []
  for i in range(cn):
    ans += [pr+i+1]*(SS.find("#")+1)
    if SS.find("#")<len(SS):
      SS = SS[SS.find("#")+1:]
    else:
      SS = ""
  ans += [pr+cn]*len(SS)
  return ans
    
cnt_pre = 0 #最初のall #no
cnt = 0 # "#"の個数
for i in range(H):
  Lin = input()
  tmp = Lin.count("#")
  if tmp == 0 and cnt == 0:
    cnt_pre +=1
  elif tmp == 0:
    print(*pS)
  else:
    pS = cv(Lin,tmp,cnt)
    for i in range(0,cnt_pre+1):
      print(*pS)
    cnt_pre = 0
  cnt += tmp