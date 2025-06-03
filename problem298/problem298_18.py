n, k = map(int, input().split())
print(sum([i >= k for i in list(map(int,input().split()))]))