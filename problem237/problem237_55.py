n = int(input())
table = []
for _ in range(n):
    x, l = map(int, input().split())
    table.append([x-l, x+l])

sorted_table = sorted(table, key=lambda x: x[1])
# print(sorted_table)
left = sorted_table[0][1]
ans = n
for i in range(1, n):
    if left <= sorted_table[i][0]:
        left = sorted_table[i][1]
    else:
        ans -= 1

print(ans)