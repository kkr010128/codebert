import copy
from sys import stdin


N = int(stdin.readline().rstrip())

L = [ int(x) for x in stdin.readline().rstrip().split()]

count = 0

for i in range(N):
    A = L.pop()
    Ln = copy.copy(L)
    for j in range(len(Ln)):
          B = Ln.pop()
          Lm = copy.copy(Ln)
          for k in Lm:
              C = k
              if ( A != B ) and ( B != C ) and ( C != A ) and ( A + B > C ) and ( B + C > A ) and ( C + A > B ):
                    count+=1
              
          

print(count) 
                
