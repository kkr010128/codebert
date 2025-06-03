n=int(input())
a=list(map(int,input().split()))
q=int(input())

st=set()
for i in range(1<<n):
  sm=0
  for j in range(n):
    if (i & (1<<j)):
      sm+=a[j]
  st.add(sm)
Q=list(map(int,input().split()))
for i in Q:
  if i in st:
    print("yes")
  else:
    print("no")
