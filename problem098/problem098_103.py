from collections import Counter

n = int(input())
s = input()

b = Counter(s)

ans = min(b["R"],b["W"])

a = 0
for i in range(b["R"]):
    if s[i] == "W":
        a += 1
        
print(min(ans,a))