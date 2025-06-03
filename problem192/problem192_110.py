def main():
  N=int(input())
  A=[int(a) for a in input().split()]
  Acnt, Aprob={}, {}
  for a in A:
    Acnt[a] = Acnt.get(a, 0) + 1
  sumA=0
  for k, a in Acnt.items():
    Aprob[k]=a*(a-1)//2
    sumA+=Aprob[k]
  #Acnt=[A.count(n) for n in range(N+1)]
  #Aprob=[Acnt[n]*(Acnt[n]-1)//2 for n in range(N+1)]
  #sumA=sum(Aprob)

  for a in A:
    ans=(Acnt[a]-1)*(Acnt[a]-2)//2
    print(ans+sumA-Aprob[a])
  
main()

