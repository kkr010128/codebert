n, k = map(int, input().split())  
argList = list(map(int, input().split()))
print(sum([h >= k for h in argList]))
