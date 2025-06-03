A = list(map(int, input().split()))

ans = 'Yes' if (len(A) - 1) == len(set(A)) else 'No'

print(ans)