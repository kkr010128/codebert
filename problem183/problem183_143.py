N=int(input())
def F(n):
    A=[]
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            A.append(i)
            if i != n // i:
                A.append(n//i)
    return A
D=F(N-1)
E=F(N)
E=sorted(E)
G=[]
for i in E[1:]:
  a=N
  while a%i==0:
    a//=i
  if a%i==1:
    G.append(i)
print(len(G)+len(D)-1)