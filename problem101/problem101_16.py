import itertools
A,B,C=map(int,input().split())
K=int(input())

l=list(range(K+1))

for c  in itertools.product(l, repeat=3):
    if sum(c) == K and A*2**c[0]<B*2**c[1] and B*2**c[1]<C*2**c[2]:
      print("Yes")
      exit(0)
print("No")
