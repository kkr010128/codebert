import sys
input=lambda: sys.stdin.readline().rstrip()
n=int(input())
A=[int(i) for i in input().split()]
mon=1000
stk=0
for i in range(n-1):
  if A[i]<=A[i+1]:
    stk+=mon//A[i]
    mon%=A[i]
  else:
    mon+=stk*A[i]
    stk=0
mon+=stk*A[-1]
print(mon)