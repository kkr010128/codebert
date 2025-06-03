n, k = list(map(int, input().split()))
list = list(map(int, input().split()))
ans = [l for l in list if l >= k]

print(len(ans))