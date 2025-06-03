n = int(input())
S, T = input().split()

ans = ""

for i in range(n):
    ans += S[i]+T[i]
    
print(ans)