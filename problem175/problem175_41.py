from collections import Counter
n = int(input())
s = input()
cnt = Counter(s)
ans = cnt["R"]*cnt["G"]*cnt["B"]
for i in range(n):
    for j in range(i+1,n):
        k = 2*j-i
        if k >= n: continue
        if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]: ans -= 1
print(ans)