n = int(input())
lst = []
for i in range(n):
    x, l = map(int, input().split())
    lst.append((x + l, x - l))

sorted_lst = sorted(lst)
num = 0
ans = n
while True:
    tmp = sorted_lst[num][0]
    for i in range(num + 1, n):
        if tmp > sorted_lst[i][1]:
            ans -= 1
        else:
            num = i
            break
        if i == n - 1:
            num = i
            break
    if num == n - 1:
        break

print(ans)