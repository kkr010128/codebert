n, k = map(int, input().split())
print(sum(int(i) >= k for i in input().split()))