n=int(input())
a=list(input().split())

l = [0 for _ in range(n+1)]
for i in a:
    l[int(i)]+=1

for j in range(1,n+1):
    print(l[j])