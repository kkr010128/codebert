def main():
  import math
  N = int(input())
  ans=0
  for i in range(1,N+1):
    for j in range(1, N+1):
      for k in range(1, N+1):
          t=math.gcd(i,j)
          t=math.gcd(t,k)
          ans+=t
        
  print(ans)
 
if __name__=='__main__':
  main()