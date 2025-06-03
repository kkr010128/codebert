S = input()

ans = 'Yes'
while S:
    if S.startswith('hi'):
        S = S[2:]
    else:
        ans = 'No'
        break

print(ans)
