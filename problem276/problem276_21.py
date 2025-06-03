from itertools import accumulate
def myAnswer(N:int,A:list) -> int:
   accum = list(accumulate(A))
   ans = 10**10
   now = accum.pop()
   for a in accum:
      if(abs(now - a - a) < ans):
         ans = abs(now - 2*a)
   return ans

   

def modelAnswer():
   tmp=1
def main():
   N = int(input())
   A = list(map(int,input().split()))
   print(myAnswer(N,A[:]))
if __name__ == '__main__':
   main()
