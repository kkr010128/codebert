N=int(input())
for x in range(1,N+1):
  if int(1.08*x)==N:
    print(x)
    break
  if x==N:
    print(":(")
