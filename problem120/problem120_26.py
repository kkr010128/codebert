N, K = list(map(int, input().split()))
p = sorted(list(map(int, input().split())), reverse=False)

print(sum(p[:K]))