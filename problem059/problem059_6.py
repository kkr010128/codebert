r, c = map(int, input().split())
tabl = [list(map(int, input().split())) for i in range(r)]
for i in range(r):
    print(" ".join(map(str, tabl[i])) + " " + str(sum(tabl[i])))
ss = ""
for i in range(c):
    ans = 0
    for j in range(r):
        ans += tabl[j][i]
    ss += str(ans) + " "
print(ss+str(sum([int(i) for i in ss.split()])))