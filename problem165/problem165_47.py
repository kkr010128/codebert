N = int(input())
ls = []
for i in range(N):
    s = input()
    ls.append(s)

newLs = list(set(ls))
print(len(newLs))
