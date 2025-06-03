import sys
input = sys.stdin.readline
# 文字列をinput()した場合、末尾に改行が入るので注意
def main(R,C,K,rcv):
  inf=float('inf')
  dp0=[[-inf,-inf,-inf,0] for _ in range(C)]
  dp1=[[-inf]*4 for _ in range(C)]
  dp0[0][3]=0
  rcv.sort(key=lambda x:C*R*x[0]+x[1])
  i=0
  nowc=0
  while i<K and rcv[i][0]==1:
    nextc=rcv[i][1]-1
    for j in range(nowc+1,nextc+1):
      dp0[j][0]=dp0[nowc][0]
      dp0[j][1]=dp0[nowc][1]
      dp0[j][2]=dp0[nowc][2]
    v=rcv[i][2]
    dp0[nextc][0]=max(dp0[nextc][0],dp0[nextc][1]+v)
    dp0[nextc][1]=max(dp0[nextc][1],dp0[nextc][2]+v)
    dp0[nextc][2]=max(dp0[nextc][2],dp0[nextc][3]+v)
    i+=1
    nowc=nextc
    for j in range(nowc+1,C):
      dp0[j][0]=dp0[nowc][0]
      dp0[j][1]=dp0[nowc][1]
      dp0[j][2]=dp0[nowc][2]
  for j in range(1,R):
    for c in range(C):
      dp0[c][3]=max(dp0[c])
      dp0[c][2]=-inf
      dp0[c][1]=-inf
      dp0[c][0]=-inf
    nowc=0
    while i<K and rcv[i][0]==j+1:
      nextc=rcv[i][1]-1
      for k in range(nowc+1,nextc+1):
        dp0[k][0]=dp0[nowc][0]
        dp0[k][1]=dp0[nowc][1]
        dp0[k][2]=dp0[nowc][2]
      v=rcv[i][2]
      dp0[nextc][0]=max(dp0[nextc][0],dp0[nextc][1]+v)
      dp0[nextc][1]=max(dp0[nextc][1],dp0[nextc][2]+v)
      dp0[nextc][2]=max(dp0[nextc][2],dp0[nextc][3]+v)
      i+=1
      nowc=nextc
    for j in range(nowc+1,C):
      dp0[j][0]=dp0[nowc][0]
      dp0[j][1]=dp0[nowc][1]
      dp0[j][2]=dp0[nowc][2]
    #print(dp0)

  print(max(dp0[-1]))


if __name__=='__main__':
  R,C,K=map(int,input().split())
  rcv=[list(map(int,input().split())) for _ in range(K)]
  #import datetime
  #print(datetime.datetime.now())
  main(R,C,K,rcv)
  #print(datetime.datetime.now())


