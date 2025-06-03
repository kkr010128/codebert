N,A,B=map(int,input().split())
sho,amri = divmod(N,(A+B))
if amri > A:
    amri = A
print(A*sho+amri)