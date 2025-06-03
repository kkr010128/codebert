N = int(input())
dic = {}
for _ in range(N):
    s = input()
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

num = 0
for key in dic:
    num = max(num, dic[key])

ans = []
for key in dic:
    if dic[key] == num:
        ans.append(key)

ans.sort()
for a in ans:
    print(a)