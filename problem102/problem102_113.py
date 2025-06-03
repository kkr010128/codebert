n,k = map(int,input().split())
a = list(map(int,input().split()))
temp,i = sum(a[:k]),k
for _ in range(n-k):
    score = temp+a[i]-a[i-k]
    print("Yes" if score>temp else "No")
    temp = score
    i+=1