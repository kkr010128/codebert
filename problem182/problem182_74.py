N, K, C = map(int, input().split())
S = str(input())

#前から貪欲に
x = 0
L = [-1] * K
p = 0
while (x < N) and (p != K):
  if S[x] == "o":
    L[p] = x
    p += 1
    x += C + 1
  else:
    x += 1

#後ろから貪欲に    
y = N - 1
R = [-1] * K
q = 0
while (y > -1) and(q != K):
  if S[y] == "o":
    R[q] = y
    q += 1
    y -= C + 1
  else:
    y -= 1
    
#print(L, R)

#LとRの被っている数に1足したものを出力
for i in range(K):
  if L[i] == R[K - i - 1]:
    print(L[i] + 1)




    
  
  
