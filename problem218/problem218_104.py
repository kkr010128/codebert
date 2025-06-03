N = int(input())

d = {}
ans = []

for i in range(N):
    S = input()
    d.setdefault(S,0)
    d[S] += 1

max = max(d.values())
for key in d.keys():
    if d[key] == max:
        ans.append(key)
        
ans = sorted(ans)

for word in ans:
    print(word)