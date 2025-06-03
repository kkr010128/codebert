L, R, d = map(int, input().split())
ans = list(map((lambda x: x % d == 0) , [i for i in range(L, R+1)])).count(True)
print(ans)