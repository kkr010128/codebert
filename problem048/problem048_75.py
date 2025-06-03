n = int(input())
a = list(map(int, input().split()))

ans = []
ans.append(min(a))
ans.append(max(a))
ans.append(sum(a))

print(" ".join(map(str, ans)))
