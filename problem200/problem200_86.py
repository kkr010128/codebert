a,b,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = []
for i in range(m):
    x.append(list(map(int, input().split())))

min_a = min(a)
min_b = min(b)
money = min_a + min_b

for i in range(m):
    kingaku = a[x[i][0]-1] + b[x[i][1]-1] - x[i][2]
    if kingaku < money:
        money = kingaku

print(money)