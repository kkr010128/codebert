a, b, m = map(int, input().split())
lista = list(map(int, input().split()))
listb = list(map(int, input().split()))

ans = min(lista)+min(listb)

for i in range(m):
    x, y, c = map(int, input().split())
    dprice = lista[x-1]+listb[y-1] - c
    if ans > dprice:
        ans = dprice

print(ans)
