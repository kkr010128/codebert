import sys
input = sys.stdin.readline
def main(R,C,K,rcv):
  inf=float('inf')
  dp0=[[-inf,-inf,-inf,0] for _ in range(C)]
  item=[[0]*C for _ in range(R)]
  for r,c,v in rcv:
    item[r-1][c-1]=v
  # dp0[c][j]:c列目の時点で残りちょうどj個取れる時の最大値
  for i in range(R):
    # i+1行目に対する操作
    # 遷移
    for j in range(C):
      if j>0:
        dp0[j][3]=max(dp0[j])
        dp0[j][0]=dp0[j-1][0]
        dp0[j][1]=dp0[j-1][1]
        dp0[j][2]=dp0[j-1][2]
      else:
        dp0[0][3]=max(dp0[0])
        dp0[0][2]=-inf
        dp0[0][1]=-inf
        dp0[0][0]=-inf 
      if item[i][j]>0:
        v=item[i][j]
        dp0[j][0]=max(dp0[j][0],dp0[j][1]+v)
        dp0[j][1]=max(dp0[j][1],dp0[j][2]+v)
        dp0[j][2]=max(dp0[j][2],dp0[j][3]+v)
  print(max(dp0[-1]))
if __name__=='__main__':
  R,C,K=map(int,input().split())
  rcv=[list(map(int,input().split())) for _ in range(K)]
  main(R,C,K,rcv)
