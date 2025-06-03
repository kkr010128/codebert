N, K = map(int, input().split())
arr = list(map(int, input().split()))

jj = 0
koho=[]
for i in range(K):
    jj+=arr[i]
    koho.append(jj)

for i in range(N-K):
    jj+=arr[i+K]
    jj-=arr[i]
    koho.append(jj)

a=max(koho)
print(a/2+(K/2))

