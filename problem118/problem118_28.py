N = int(input())
ans = 0
for i in range(1,N+1): #1-N
  first = i; kosu = N//i
  end = kosu*i
  temp = (first+end)*kosu//2
  ans += temp
print(ans)
