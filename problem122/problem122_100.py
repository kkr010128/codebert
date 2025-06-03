def main():
  N=int(input())
  A=list(map(int,input().split()))
  s=sum(A)
  Q=int(input())
  d=[0]*(10**5 +1)#各数字の個数
  for i in A:
    d[i]+=1

  for i in range(Q):
    B,C=map(int,input().split())
    s += (C-B)*d[B]
    print(s)
    d[C]+=d[B]
    d[B]=0

if __name__ == "__main__":
    main()