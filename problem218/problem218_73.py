#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [input() for _ in range(n)]


n = int(input())
s = [input() for _ in range(n)]


h = {}

for i in range(n):
    if (s[i] in h):
        h[s[i]] += 1
    else:
        h[s[i]] = 1


ans = []
highScore = max(h.values())

for k,v in h.items():
    if v== highScore:
        ans.append(k)

ans.sort()

for i in range(len(ans)):
    print(ans[i])


