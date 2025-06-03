N=int(input())
A= list(map(int,input().split()))

AA=sorted(A)
B=1
for i in range(N):
    B=B*AA[i]
    if B>10**18:
      B=-1
      break

print(B)