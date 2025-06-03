A,B,C=map(int,input().split())
K=int(input())
result='No'

while A>=B:
  K-=1
  B*=2
while B>=C:
  K-=1
  C*=2

if K>=0 and  C>B and B>A:
  result='Yes'

print(result)