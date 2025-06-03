X,K,D = map(int,input().split())
X = abs(X)
 
if X <= K * D :
  if (K - X // D) % 2 == 1 :
    answer = abs(X % D - D)
  else :
    answer = X % D
else :
  answer = X - K * D
  
print(answer)