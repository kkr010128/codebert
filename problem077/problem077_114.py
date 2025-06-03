n = list(map(int,input().split()))


ans = n[1] * n[3]
ans = max(n[0]*n[2],ans)
ans = max(n[0]*n[3],ans)
ans = max(n[1]*n[2],ans)
ans = max(n[1]*n[3],ans)
print(ans)