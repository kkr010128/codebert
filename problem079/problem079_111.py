from scipy import special

S = int(input())
top = S // 3
if top == 0:
    print(0)
    exit()

ans = 1
mod = 10 ** 9 + 7
for i in range(2, top + 1):
    t = S - 3 * i
    i -= 1
    ans += special.comb(t+i, i, True)
print(ans % (mod))
