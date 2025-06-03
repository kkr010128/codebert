ans = []
for i in range(4):
    for j in range(13):
        ans.append("SHCD"[i] + " " + str(j + 1))

n = int(input())
for i in range(n):
    a = input()
    ans.remove(a)

if len(ans) > 0:
    print("\n".join(ans))
