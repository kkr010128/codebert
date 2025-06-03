h,n = map(int,input().split())
a = list(map(int,input().split()))

suma = sum(a)

print('Yes' if h - suma <= 0 else 'No')