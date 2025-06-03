n, m = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)
総投票数 = sum(a)
x = 総投票数 / (4 * m)
for i in range(m):
    if a[i] < x:
        flag = 0
        break
else:
    flag = 1
print(["No", "Yes"][flag])