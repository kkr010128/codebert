h,n = map(int, input().split())
a = list(map(int, input().split()))
print('Yes' if h-sum(a) <= 0 else 'No')