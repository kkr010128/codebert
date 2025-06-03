N = int(input())
S, T = input().split()
S_list = list(S)
T_list = list(T)

ans = ""

for i, j in zip(S_list, T_list):
    ans += i + j

print(ans)
