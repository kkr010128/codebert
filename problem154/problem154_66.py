N, K = map(int, input().split())

people = []
 
for i in range(K):
  _ = input()
  a = list(map(int, input().split()))
  people += a
  
print(N - len(set(people)))