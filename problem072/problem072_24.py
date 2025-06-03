N = int(input())
D1, D2 = [], []
for i in range(N):
  li = list(map(int,input().split()))
  D1.append(li[0])
  D2.append(li[1])

for i in range(N-2):
  if D1[i]==D2[i] and D1[i+1]==D2[i+1] and D1[i+2]==D2[i+2]:
    print('Yes')
    break
else:
  print('No')
