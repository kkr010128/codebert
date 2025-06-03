from sys import exit
import math

def main():
  N = int(input())
  ran = int(math.sqrt(N))
  ans = N
  
  for i in range(1,ran+1):
    if N % i == 0:
      #print('L')
      if N / i + i <= ans + 1:
        ans = ((N / i) + i) -2
        #print(i)
  
  print(int(ans))
  
  
  
main()