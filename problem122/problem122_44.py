def main():
  N=int(input())
  A=list(map(int,input().split()))
  s=sum(A)
  Q=int(input())
  d=[0]*(10**5 +1)#各数字の個数
  ans=[]
  for i in A:
    d[i]+=1

  for i in range(Q):
    B,C=map(int,input().split())
    s += (C-B)*d[B]
    ans.append(s)
    d[C]+=d[B]
    d[B]=0

  print("\n".join(map(str, ans)))
  #BC入力ごとに出力するよりまとめて出力した方が倍くらい早い

if __name__ == "__main__":
    main()