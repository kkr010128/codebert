# Common Raccoon vs Monster
H, N = map(int,input().split())
A = list(map(int, input().split()))
ans = ['No', 'Yes'][sum(A) >= H]
print(ans)