A,B,C = map(int, input().split())
K = int(input())

n = 0

while (A >= B):
  B = 2*B
  n +=1
  
while B>=C:
  C = 2*C
  n += 1
  
#print(A,B,C,n)

if n <= K:
  print('Yes')
else:
  print('No')
