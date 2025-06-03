X,K,D = map(int,input().split())
dist = abs(X)
rem = K
count = min(dist//D,K)
dist -= count*D
rem -= count
if rem % 2 == 1:
  dist -= D
print(abs(dist)) 
