n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()

ans = 0
prevs = [''] * k
for i in range(n//k+1):
  #print(i)
  #print(prevs)
  for j in range(i*k, (i+1)*k):
    if j >= n:
      break
    prevs_i = j%k
    prev = prevs[prevs_i]
    #print(prev)
    
    if t[j] == 'r':
      if prev == 'p':
        prevs[prevs_i] = ''
      else:
        prevs[prevs_i] = 'p'
        ans += p
    elif t[j] == 's':
      if prev == 'r':
        prevs[prevs_i] = ''
      else:
        prevs[prevs_i] = 'r'
        ans += r
    elif t[j] == 'p':
      if prev == 's':
        prevs[prevs_i] = ''
      else:
        prevs[prevs_i] = 's'
        ans += s
print(ans)