s, t = input().split()
d = {}
d[s] , d[t] = map(int, input().split())
d[input()]-=1
for i in d.values(): print(i, end = ' ')