N,K=map(int,input().split())
lista=[]
for i in range(K):
    d=input()
    A=list(map(int,input().split()))
    lista.extend(A)
print(N-len(list(set(lista))))