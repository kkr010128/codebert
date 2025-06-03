n, k = map(int, input().split())

tmp = n%k

print(min(tmp, abs(tmp-k)))