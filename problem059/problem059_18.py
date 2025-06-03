r, c = map(int, raw_input().split(" "))
table1 = [[0 for j in range(c)] for i in range(r)]
for i in range(r):
    table1[i] = map(int, raw_input().split(" "))

table2 = [0 for j in range(c+1)]
ans = ""
for i in range(r):
    tmp = 0
    for j in range(c):
        ans += str(table1[i][j]) + " "
        tmp += table1[i][j] 
        table2[j] += table1[i][j]
    ans += str(tmp) + "\n"
for j in range(c+1):
    ans += str(table2[j])
    table2[c] += table2[j]
    if j!=c:
        ans += " "

print ans