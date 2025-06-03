A, B, C = list(map(int,input().split()))
K = int(input())

ans = 'No'
while K >= 0:
    if A < B:
        break
    B *= 2
    K -= 1

while K >= 0:
    if B < C:
        ans = 'Yes'
        break
    C *= 2
    K -= 1

print(ans)