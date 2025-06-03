n = int(input())
toko = [int(i) for i in input().split()]

ans = [int(0) for i in range(n)]

for j in range(n): ##01234
  ans[toko[j]-1] = j + 1
  
print(' '.join(map(str, ans)))