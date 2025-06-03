A, B, C, D = map(int, input().split())

while(True):
    C = C - B
    if C <= 0:
        ans = 'Yes'
        break

    A = A - D
    if A <= 0:
        ans = 'No'
        break

print(ans)