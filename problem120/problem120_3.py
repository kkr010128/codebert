n,k =map(int,input().split())

l = list(map(int,input().split()))

l = sorted(l)
print(sum(l[0:k]))
