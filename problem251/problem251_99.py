N, K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()

ans = 0
hands = ["" for _ in range(N)]

for k in range(K):
  if T[k] == "r":
    ans += P
    hands[k] = "p"
  elif T[k] == "s":
    ans += R
    hands[k] = "r"
  else:
    ans += S
    hands[k] = "s"
    
    
for n in range(K,N):
  if T[n] == "r":
    if hands[n-K] != "p":
      ans += P
      hands[n] = "p"
    else:
      hands[n] = "x"
      
  elif T[n] == "s":
    if hands[n-K] != "r":
      ans += R
      hands[n] = "r"
    else:
      hands[n] = "x"
      
  else:#T[n] == "p"
    if hands[n-K] != "s":
      ans += S
      hands[n] = "s"
    else:
      hands[n] = "x"

print(ans)
