K,N = map(int,input().split())
cc = list(map(int,input().split()))
min_length = max(cc)-min(cc)
for i in range(1,N):
  Length = K-cc[i]+cc[i-1]
  min_length = min(min_length,Length)
print(min_length)