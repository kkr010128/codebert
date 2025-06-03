n = int(input())
st = list(map(int,input().split()))
st.sort(reverse = True)
count = 0

for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      if (st[i] != st[j] != st[k]) and (st[i] < st[j] + st[k]):
        count += 1
        
print(count)
