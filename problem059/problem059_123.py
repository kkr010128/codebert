import sys

printf = sys.stdout.write


mat = []
new_map = []

r,c = map(int, raw_input().split())
for i in range(r):
    mat = map(int, raw_input().split())
    new_map.append(mat)


for i in range(r):
    new_map[i].append(sum(new_map[i][:]))
    for j in range(c):
        print new_map[i][j],
    printf(" " + str(new_map[i][j + 1]) + "\n")


for j in range(c + 1):
    a = 0
    for i in range(r):
        a += new_map[i][j]
    if j == c:
        printf(" " + str(a) + "\n")
        break
    else:
        print a,