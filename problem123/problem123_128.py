N = int(input())
a = list(map(int, input().split()))
S = 0
for aa in a:
    S ^= aa
ans = ""
for ai in a:
    ans += f'{str(S ^ ai)} '
print(ans.rstrip())
