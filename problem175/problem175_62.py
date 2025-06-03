from itertools import permutations

n = int(input())
s = input()

out = 0
ans = s.count("R")*s.count("G")*s.count("B")

combi = list(permutations(["R","G","B"],3))

for i in range(1,n):
    for j in range(n-i*2):
        if (s[j], s[j+i], s[j+i*2]) in combi:
            ans -= 1

print(ans)