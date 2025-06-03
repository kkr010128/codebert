import sys

"""
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x = read().rstrip().decode()
"""

N = int(input())
L = list(map(int,input().split()));
L.sort();

def solve():
    ret = 0
    for i in range(0,N-2):
      for j in range(i+1,N-1):
        for k in range(j+1,N):
          if L[i] != L[j] and L[j] != L[k] and L[i]+L[j] > L[k]:
            ret += 1
            #print(i,j,k)
    
    return ret

print(solve())