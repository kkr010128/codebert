S = str(input())
T = str(input())

ans = 'Yes' if T[:len(S)] == S else 'No'

print(ans)